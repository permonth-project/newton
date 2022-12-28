import os
from tqdm import tqdm
from datetime import datetime
import pandas as pd
from utils import module_path, starttime, starttime_str
import utils
from src.set_logging import log_path, logger
from pprint import pprint


class Craigslist:
    def __init__(self, query, region):
        self.BASE_URL = 'https://vancouver.craigslist.org'
        self.REGION = region
        self.QUERY = query
        self.PAGE_IDX = 0
        self.QUERY_URL = f"{self.BASE_URL}/search/sss?&query={self.QUERY.replace(' ', '%20')}"
        self.result_row = None
        self.soup = utils.get_soup(self.QUERY_URL)
        logger.info('Initializing Craigslist scraper')

    def reset_url(self, page_idx):
        self.PAGE_IDX = page_idx
        self.QUERY_URL = f"{self.BASE_URL}/search/sss?s={page_idx}&query={self.QUERY.replace(' ', '%20')}"
        self.soup = utils.get_soup(self.QUERY_URL)

    def get_result_row(self):
        search_res = self.soup.find('ul', {'id': 'search-results'})
        self.result_row = search_res.find_all('li', {"class": 'result-row'})
        return self.result_row

    def extract_info(self, row):
        result_link = row.find('a', 'result-image').get('href')
        result_price = row.find('span', 'result-price').text if row.find('span', 'result-price') is not None else None
        result_date = row.find('time', 'result-date').get('datetime')
        result_title = row.find('a', 'result-title').text if row.find('a', 'result-title') is not None else None
        result_hood = row.find('span', 'result-hood').text if row.find('span', 'result-hood') is not None else None

        return {
            'result_link': result_link,
            'result_price': result_price,
            'result_date': result_date,
            'result_title': result_title,
            'result_hood': result_hood,
            **self.extract_result_link(result_link)
            }

    def extract_result_link(self, link):
        soup = utils.get_soup(link)
        postingdate = ''
        post_id = ''
        attr_dict = ''
        map_data_accuracy = ''
        map_data_longitude = ''
        map_data_latitude = ''

        ## get map info
        mapbox = soup.find('div', {'id': 'map'})
        if mapbox is not None:
            map_data_accuracy = mapbox.get('data-accuracy')
            map_data_longitude = mapbox.get('data-longitude')
            map_data_latitude = mapbox.get('data-latitude')

        ## get product attributes
        attrgroup = soup.find('p', 'attrgroup')
        if attrgroup is not None:
            focus_text = attrgroup.text
            focus_list = [t for t in focus_text.split('\n') if (t != '') and (t is not None)]
            focus_dict = {attr.split(':')[0]: attr.split(':')[1] for attr in focus_list if ':' in attr}
            attr_dict = focus_dict
        else:
            attr_dict = dict()

        ## get main image URL
        main_img_url = soup.find('div', 'slide first visible').img.get('src') \
            if soup.find('div', 'slide first visible') is not None else ''

        ## get posting body
        posting_body = soup.find('section', {'id': 'postingbody'}).text.replace('QR Code Link to This Post', '').strip() \
            if soup.find('section', {'id': 'postingbody'}) is not None else ''

        ## get notices
        user_notices = soup.find('ul', 'notices').find_all('li')

        ## get postinginfos
        for s in soup.find_all('p', 'postinginfo'):
            if s.time:
                postingdate = s.time.get('datetime')
            if 'post id' in s.text:
                post_id = s.text.split('post id: ')[1].strip()

        return {
            'map_data_accuracy': map_data_accuracy,
            'map_data_longitude': map_data_longitude,
            'map_data_latitude': map_data_latitude,
            'main_img_url': main_img_url,
            'posting_body': posting_body,
            'user_notices': user_notices,
            'postingdate': postingdate,
            'post_id': post_id,
            **attr_dict
            }

    def get_page_range(self):
        range_from = self.soup.find('span', "button pagenum").find('span', 'rangeFrom').text
        range_to = self.soup.find('span', "button pagenum").find('span', 'rangeTo').text
        total_count = self.soup.find('span', "button pagenum").find('span', 'totalcount').text
        logger.info(f"Total products: {total_count}")
        return range_from, range_to, total_count

    def get_info(self):
        range_from, range_to, total_count = self.get_page_range()
        info_list = []
        for page_idx in range(int(range_from), int(total_count), int(range_to)):
            logger.info(f"Scraping from page index: {page_idx}")
            page_idx = page_idx - 1
            if page_idx != 0:
                self.reset_url(page_idx)
            for row in tqdm(self.get_result_row()):
                try:
                    extract_res = self.extract_info(row)
                except AttributeError:
                    continue
                info_list.append(extract_res)
        df = pd.DataFrame(info_list)
        df.insert(0, '_region', self.REGION)
        df.insert(0, '_product', self.QUERY)
        df.insert(0, '_query_url', self.QUERY_URL)
        df = df.loc[df.astype(str).drop_duplicates().index]
        logger.info(f"Successfully completed scraping")
        logger.info(f"Result below. Total rows: {len(df.index)}")
        logger.info(f"\n{df}")
        return df


# class Carousell:
#     def __init__(self, query):
#         self.json_data = None
#         self.headers = None
#         self.BASE_URL = 'https://www.carousell.com.hk'
#         self.QUERY = query
#         self.QUERY_URL = f"{self.BASE_URL}/search/{self.QUERY.replace(' ', '%20')}"
#
#     def get_init_page(self):
#
#
#     def get_next(self):
#         self.headers = {
#             'authority': 'www.carousell.com.hk',
#             'accept': '*/*',
#             'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ko;q=0.6',
#             'cache-control': 'no-cache',
#             'content-type': 'application/json',
#             'cookie': '_t2=HwRlSrXJL6; WZRK_G=f37cfecc16cd484e9be1d030ff1b1d15; _fbp=fb.2.1657848388188.1967208570; fbm_379979055398817=base_domain=; _gcl_aw=GCL.1663565905.CjwKCAjwg5uZBhATEiwAhhRLHo_iTHEXn6uw6lVQuTfkTSF-usQGWQxtY2ORRQTq52ee1X6JOTXhlBoCqUAQAvD_BwE; _gac_UA-32231169-26=1.1663565908.CjwKCAjwg5uZBhATEiwAhhRLHo_iTHEXn6uw6lVQuTfkTSF-usQGWQxtY2ORRQTq52ee1X6JOTXhlBoCqUAQAvD_BwE; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%20%221837809220d290-03283e10b2c315-1a525635-16a7f0-1837809220e6bc%22%2C%22%24device_id%22%3A%20%221837809220d290-03283e10b2c315-1a525635-16a7f0-1837809220e6bc%22%2C%22site_type%22%3A%20%22similarweb%20extension%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _gcl_au=1.1.528049427.1666931473; g_state={"i_p":1670045235463,"i_l":1}; _t=a%3D38L7yhjg4i%26t%3D1670385466944; _gid=GA1.3.1305131038.1670589413; _csrf=aGRLPRNynDz1fZFeyezbulIO; latra=1670630400000; __qca=I0-1507387796-1670641457961; siv_2=94305d5d-d5aa-4f92-b4cc-be3cb1a5237a; _gaclientid=380327976.1657848388; _gasessionid=20221210|08470039; cto_bundle=LBAApV9LVXAwcVlUTXdlc2RsVWY2d2g5dGduOVYwUmlySiUyQjZhYWRZaGp1QlVLdTYwcUlrNXNkTkVxcUZrdXZyVERhU2pQVHNDOTc4dE1ndktLbVlqYkFqMTU4aThIajZPUkZFcVlaYzE5THJqaXVYaSUyQjk1eDhqclJ3M0ZocUJGckZoWFJ0Y3I2MkdzYnM4NlY4RVN5WmJ1dXA1U1puTnZOaWNRbUdWakxDeDI4SVlVJTNE; _gahitid=22:09:07; _dc_gtm_UA-32231169-26=1; _ga_BTYMG7D1RH=GS1.1.1670681229.35.1.1670681347.59.0.0; _ga=GA1.1.380327976.1657848388; WZRK_S_8R9-448-845Z=%7B%22p%22%3A2%2C%22s%22%3A1670681229%2C%22t%22%3A1670681347%7D',
#             'csrf-token': 'bReeDtiB-DfQ5H_cYCiOIbYkcHin-WSw_DSU',
#             # 'origin': 'https://www.carousell.com.hk',
#             # 'pragma': 'no-cache',
#             # 'referer': 'https://www.carousell.com.hk/search/iphone%2013/?searchId=-mb74o',
#             # 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#             # 'sec-ch-ua-mobile': '?0',
#             # 'sec-ch-ua-platform': '"macOS"',
#             # 'sec-fetch-dest': 'empty',
#             # 'sec-fetch-mode': 'cors',
#             # 'sec-fetch-site': 'same-origin',
#             # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#             # 'y-build-no': '2',
#             # 'y-platform': 'web',
#             # 'y-x-request-id': 'o5FIAt2ZVgQx17co',
#             }
#
#         self.json_data = {
#             'bestMatchEnabled': True,
#             'canChangeKeyword': False,
#             'count': 48,
#             'countryCode': 'HK',
#             'countryId': '1819730',
#             'filters': [],
#             'includeEducationBanner': True,
#             'includeSuggestions': False,
#             'locale': 'en',
#             'prefill': {},
#             'query': 'iphone 13',
#             # 'searchContext': '0a0208301a0408d2886f220d0a096970686f6e6520313378013204080078013a02180742060801100118004a0620012801400150015a020801',
#             # 'session': 'eyJhZ2dyZWdhdGVfY291bnQiOjQ4LCJhcHBsaWVkX2NjaWQiOiIiLCJjb250ZW50Ijp7ImludGVybmFsX2FkcyI6eyJwYWdlX251bWJlciI6MX0sImxpc3RpbmdfY2FyZC1ibG9jayI6eyJjaHVua19udW1iZXIiOjAsImNodW5rX3N0YXJ0X29mZnNldCI6MCwiY3JlYXRlZF9hdCI6IjIwMjItMTItMTBUMTQ6MDk6MDVaIiwib2Zmc2V0Ijo0OCwidmVyc2lvbiI6IjUzOTU0OTE3LTkxMzMtNDY2Ni1hYzk2LWE5ZTViNzllYTdjNiJ9fSwiZW5mb3JjZV9jYXRlZ29yeV9maWx0ZXIiOmZhbHNlLCJmaWVsZHNldF9jY2lkIjoiNTY0MyIsInBhZ2Vfc2l6ZSI6NDgsInF1c3ZjX3Jlc3AiOiJDaEFLQkRVek5UY1ZBYmhUUGgwQUFJQS9DaEFLQkRVek1qWVZlMXZuUFIxOTN3cy9DaEFLQkRVek1Ea1YxL0hhUFIxZVhnUS9FaEFLQkRVek1qVVY1Z1RuUGgwQUFJQS9FaEFLQkRVek5UY1ZBYmhUUGgzVm5PbytHaEFLQkRVMk5ETVZqR3A1UHgwQUFJQS9HZ1lLQkRVek1qVWFCZ29FTlRNMU55SXhDZ2xwY0dodmJtVWdNVE1TQ1dsd2FHOXVaU0F4TTBnQ1dnQmlDV2x3YUc5dVpTQXhNNG9CQ1dsd2FHOXVaU0F4TXpJQ0NBRkNFQW9FTlRZME14V01hbmsvSFFBQWdEOUNCZ29FTlRNeU5VSUdDZ1ExTXpVMyIsInJlcV9oYXNfY2hhbmdlZCI6ZmFsc2UsInNlYXJjaF9wYXJhbXMiOiJHZ0lJTUNvRUNOS0lieklOQ2dscGNHaHZibVVnTVRONEFVSUNDQUZLQWhnSFVnUUlBUkFCV2dZZ0FTZ0JRQUZnQVdvQ0NBRT0iLCJzZXNzaW9uX2lkIjoiMTVmNGFjNjMtNDQ2Yy00MGI2LTlhNGYtYjRjOTE1N2RmOTJhIiwic3VnZ2VzdGVkX2NhdGVnb3J5X3R5cGUiOjIsInN1Z2dlc3RlZF9jY2lkIjoiNTY0MyJ9',
#             }
#
#         response = requests.post(
#             'https://www.carousell.com.hk/ds/search/cf/4.0/search/',
#             # params=params,
#             # cookies=cookies,
#             headers=self.headers,
#             json=self.json_data,
#             )
#         return response
#
#     # def get_collection_links(self, collection='get_all'):
#     #     coll_url = '/collections'
#     #     soup = get_soup(self.BASE_URL + coll_url)
#     #     if collection != 'get_all':
#     #         return [soup.find('p', text=str(collection)).find_parent()['href']]
#     #
#     #     links = []
#     #     collections = soup.find('div', {'data-section-id': 'list-collections-template'}).findChildren()
#     #     for child in collections:
#     #         try:
#     #             link = child.find('a', {'class': 'grid-link'}, href=True)['href']
#     #             links.append(link)
#     #         except TypeError:
#     #             continue
#     #     return links
#     #
#     # def get_product_links(self):
#     #     collection_links = self.get_collection_links()
#     #     product_links = []
#     #     for link in tqdm(collection_links, total=len(collection_links)):
#     #         soup = get_soup(self.BASE_URL + link)
#     #         product_grp_raw = soup.find('div', {'class': 'grid-uniform grid-link__container'})
#     #         product_links_raw = product_grp_raw.find_all('a', {'class': 'grid-link text-center'})
#     #         product_links += [product['href'] for product in product_links_raw]
#     #     return product_links
#     #
#     # @staticmethod
#     # def scrape_product_data(url):
#     #     soup = get_soup(url)
#     #     scraped_time = datetime.today()
#     #     main_divs = soup.find_all('div', {'class': 'grid__item post-large--one-half'})
#     #     main = main_divs[1]
#     #     for idx, div in enumerate(main_divs):
#     #         if 'product-single__photos' not in div.findChild()['class']:
#     #             main = div
#     #             break
#     #
#     #     brand = main.find_all('span', {'itemprop': 'brand'})[0].get_text(strip=True)
#     #     name = main.find_all('h1', {'itemprop': 'name'})[0].get_text(strip=True)
#     #     priceCurrency = main.find_all('meta', {'itemprop': 'priceCurrency'})[0]['content']
#     #     availability = main.find_all('link', {'itemprop': 'availability'})[0]['href'].split('/')[-1]
#     #     ProductPrice = main.find_all('span', {'id': 'ProductPrice'})[0].get_text(strip=True).strip()
#     #     ComparePrice = main.find_all('s', {'id': 'ComparePrice'})[0].get_text(strip=True).strip()
#     #     product_description = main.find('div', {'class': 'product-description rte'}).find_all('p')
#     #     product_note_dict = {'product_note': text for text in [p.get_text(strip=True) for p in product_description] if
#     #                          ':' not in text[:20]}
#     #     product_details_dict = {text.split(':')[0]: text.split(':')[1] for text in
#     #                             [p.get_text(strip=True) for p in product_description] if ':' in text[:20]}
#     #
#     #     consolidated_data = dict(
#     #         scraped_time=scraped_time,
#     #         url=url,
#     #         brand=brand,
#     #         name=name,
#     #         priceCurency=priceCurrency,
#     #         availability=availability,
#     #         ProductPrice=ProductPrice,
#     #         ComparePrice=ComparePrice,
#     #         **product_note_dict,
#     #         **product_details_dict
#     #         )
#     #
#     #     return consolidated_data
#     #
#     # def get_products(self):
#     #     product_links = self.get_product_links()
#     #     product_data_list = []
#     #     for link in tqdm(product_links, total=len(product_links)):
#     #         print(link)
#     #         url = self.BASE_URL + link
#     #         product_data = self.scrape_product_data(url)
#     #         product_data_list.append(product_data)
#     #     df = pd.DataFrame(product_data_list)
#     #
#     #     return df


def main():
    ## Get iPhone models
    all_iphone_models, current_iphone_models = utils.get_iphone_models(logger=logger)
    all_iphone_models.reverse()
    current_iphone_models.reverse()

    ## Scrape data from Craigslist
    df_data = pd.DataFrame()
    for model in current_iphone_models:
        logger.info(f"Scraping model: {model}")
        craigslist = Craigslist(model, 'vancouver')
        df = craigslist.get_info()
        df_data = pd.concat([df_data, df])

    ## Save scraped data in CSV and Picklefile
    df_data.to_csv(f'craigslist_{starttime_str.replace(" ", "T")}.csv')
    df_data.to_pickle(f'craigslist_{starttime_str.replace(" ", "T")}.pickle')
    logger.info('=' * 65)
    logger.info('Scraper ended at {0}'.format(datetime.fromtimestamp(starttime).strftime('%Y%m%d %H:%M:%S')))
    logger.info('=' * 65)


if __name__ == "__main__":
    main()


