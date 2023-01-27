import pandas as pd
from scraper.utils import module_path, starttime, starttime_str
from scraper import utils
from scraper.src.set_logging import log_path, logger
from scraper.src.scrapers import Craigslist
from scraper.src import db
from datetime import datetime
import os
import traceback
import time
import gc
import traceback


def get_craigslist():
    ## Get iPhone models
    all_iphone_models, current_iphone_models = utils.get_iphone_models(logger=logger)
    all_iphone_models.reverse()
    current_iphone_models.reverse()
    csv_fname = f'craigslist_{starttime_str.replace(" ", "T")}.csv'
    csv_fpath = os.path.join(module_path, 'data', csv_fname)

    ## Scrape data from Craigslist
    df_data = pd.DataFrame()
    for model in current_iphone_models:
        if os.path.exists(csv_fpath):
            pd.read_csv(csv_fpath)
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
        df_data.to_csv(csv_fpath)
        gc.collect()
    logger.info('=' * 65)
    logger.info('Scraper ended at {0}'.format(datetime.fromtimestamp(starttime).strftime('%Y%m%d %H:%M:%S')))
    logger.info('=' * 65)


def main():
    try:
        get_craigslist()
    except:
        logger.error(traceback.print_exc())
        pass
    try:
        db.insert_listings()
    except:
        logger.error(traceback.print_exc())
        pass


if __name__ == "__main__":
    main()
