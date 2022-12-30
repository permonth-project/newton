import pandas as pd
from utils import module_path, starttime, starttime_str
import utils
from src.set_logging import log_path, logger
from src.scrapers import Craigslist
from datetime import datetime
import os
import traceback
import time


def get_craigslist():
    ## Get iPhone models
    all_iphone_models, current_iphone_models = utils.get_iphone_models(logger=logger)
    all_iphone_models.reverse()
    current_iphone_models.reverse()

    ## Scrape data from Craigslist
    df_data = pd.DataFrame()
    for model in current_iphone_models:
        logger.info(f"Scraping model: {model}")
        try:
            craigslist = Craigslist(model, 'vancouver')
            df = craigslist.get_info()
        except AttributeError:
            traceback.print_exc()
            continue
        except ConnectionResetError:
            traceback.print_exc()
            continue
        df_data = pd.concat([df_data, df])
        time.sleep(15)

    ## Save scraped data in CSV and Picklefile
    df_data.to_csv(os.path.join('data', f'craigslist_{starttime_str.replace(" ", "T")}.csv'))
    df_data.to_pickle(os.path.join('data', f'craigslist_{starttime_str.replace(" ", "T")}.pickle'))
    logger.info('=' * 65)
    logger.info('Scraper ended at {0}'.format(datetime.fromtimestamp(starttime).strftime('%Y%m%d %H:%M:%S')))
    logger.info('=' * 65)


def main():
    get_craigslist()


if __name__ == "__main__":
    main()
