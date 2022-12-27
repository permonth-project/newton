import os
from datetime import date, datetime
import time
import requests
from typing import Iterable
import webbrowser
from bs4 import BeautifulSoup
import unicodedata
import pandas as pd


"""Set up path"""
module_path = os.path.dirname(os.path.abspath(__file__))

today = date.today().strftime("%Y%m%d")
starttime = time.time()
starttime_str = datetime.fromtimestamp(starttime).strftime('%Y%m%d %H:%M:%S')


def get_iphone_models(logger):
    logger.info(f"Retrieving iPhone models")
    URL = 'https://en.wikipedia.org/wiki/IPhone'
    soup = get_soup(URL)
    tbl = soup.find_all('table', {'class': 'wikitable'})
    for t in tbl:
        if t.find('caption').find('div', 'navbar plainlinks hlist navbar-mini') is not None:
            cap = t.find('caption').text
            if 'all' in cap.lower() and 'iphone' in cap.lower():
                df = pd.read_html(unicodedata.normalize('NFKD', str(t)))[0]
                df = df[~df['model'].squeeze().str.contains("Legend")]
                all_iphone_models = df['model'].squeeze().values.tolist()
                all_iphone_models = list(flatten([m.split('/') for m in all_iphone_models]))

                df_current_model = df[df['support']['ended']['ended'] == 'current']
                current_iphone_models = df_current_model['model'].squeeze().values.tolist()
                current_iphone_models = list(flatten([m.split('/') for m in current_iphone_models]))
                logger.info(f"Done")
                logger.info(f"All iPhone models: {all_iphone_models}")
                logger.info(f"Current iPhone models: {current_iphone_models}")
                return all_iphone_models, current_iphone_models
    logger.error(f"iPhone models not found")
    return [], []


def open_html(html):
    with open(f'{os.getcwd()}/test.html', 'w') as f:
        f.write(html)
        f.flush()

    webbrowser.open(f"file:///{f.name}")


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup


def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x.strip()