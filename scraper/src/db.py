import mysql.connector
import utils
from utils import module_path
from src.set_logging import log_path, logger
from sqlalchemy import create_engine
import difflib
import os
from dotenv import load_dotenv
import re
from datetime import datetime
import pandas as pd
import difflib
import traceback


load_dotenv()

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPORT = os.getenv('DBPORT')
DBPASSWORD = os.getenv('DBPASSWORD')
DATABASE = os.getenv('DATABASE')

sqlalchemy_engine = create_engine(f'mysql+pymysql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DATABASE}', echo=False)

con = mysql.connector.connect(
    host=DBHOST,
    user=DBUSER,
    port=DBPORT,
    password=DBPASSWORD,
    database=DATABASE
    )
cur = con.cursor(buffered=True)


def insert_orig_specs():
    ## insert iphone specs to product_orig table
    iphone_specs = utils.get_iphone_official_specs()
    iphone_specs = iphone_specs.iloc[::-1]
    iphone_specs.reset_index(drop=True, inplace=True)
    iphone_specs.to_sql(name='product_orig', con=sqlalchemy_engine, if_exists='append', index=False)


def get_current_products(df):
    ## add 'current' column to indicate if the product model is the currently supported model
    all_iphone_models, current_iphone_models = utils.get_iphone_models(logger)
    for model in df.itertuples():
        m = model.model_name
        df.at[model.Index, 'current'] = 0
        if difflib.get_close_matches(
                m.replace(' generation', '').replace('mini', 'Mini'), current_iphone_models, cutoff=0.95):
            df.at[model.Index, 'current'] = 1
    return df


def insert_specs_explode():
    iphone_specs = utils.get_iphone_official_specs()
    ## insert iphone specs into separate rows
    for model in iphone_specs.itertuples():
        if not isinstance(model.color, list) and not isinstance(model.color, float):
            iphone_specs.at[model.Index, 'color'] = [c.strip().capitalize() for c in model.color.split(',')]
        if not isinstance(model.capacity, list) and not isinstance(model.capacity, float):
            iphone_specs.at[model.Index, 'capacity'] = [
                c.strip() if ('GB' in c) or ('TB' in c) else f"{c} {model.capacity.strip()[-2:]}" for c in
                model.capacity.split(',')]
    iphone_specs_explode = iphone_specs\
        .explode(column=['color'])\
        .explode('capacity')[['model_name', 'color', 'capacity']]\
        .apply(lambda x: x.str.strip())
    iphone_specs_explode = get_current_products(iphone_specs_explode)
    iphone_specs_explode.reset_index(drop=True, inplace=True)
    iphone_specs_explode.to_sql(name='product', con=sqlalchemy_engine, if_exists='append', index=False)


class DatabaseQuery:
    def __init__(self, row):
        self.cur = con.cursor(buffered=True)
        self.row = row
        return

    def get_region(self):
        self.cur.execute(
            f"""
                SELECT id FROM mydb.region 
                WHERE region='{self.row._3.strip()}'
            """)
        res = self.cur.fetchall()
        if len(res) == 0:
            self.cur.execute(
                f"""
                    INSERT INTO mydb.region VALUES (
                        default, 
                        '{self.row._3.strip()}'
                    )
                """)
            con.commit()
            return self.cur.lastrowid
        return res[0][0]

    def get_hood(self):
        self.cur.execute(
            f"""
                SELECT id FROM mydb.hood 
                WHERE hood='{self.row.result_hood.strip()}'
            """)
        res = self.cur.fetchall()
        if len(res) == 0:
            self.cur.execute(
                f"""
                    INSERT INTO mydb.hood VALUES (
                        default, 
                        '{self.row.result_hood.strip()}'
                    )
                """)
            con.commit()
            return self.cur.lastrowid
        return res[0][0]

    def get_query(self):
        self.cur.execute(
            f"""
                SELECT id FROM mydb.filter_query 
                WHERE url='{self.row._1.strip()}' 
                AND body='{self.row._2.strip()}' 
                AND region_id='{self.get_region()}' 
            """)
        res = self.cur.fetchall()
        if len(res) == 0:
            self.cur.execute(
                f"""
                    INSERT INTO mydb.filter_query VALUES (
                        default, 
                        '{self.row._1.strip()}',
                        '{self.row._2.strip()}',
                        '{self.get_region()}'
                    )
                """)
            con.commit()
            return self.cur.lastrowid
        return res[0][0]


def insert_listings(df_listings):
    logger.info('=' * 65)
    logger.info(f"Starting data insertion")
    # data_list = os.listdir('data')
    # file_dates_only = [re.match(r'craigslist_([0-9]*T[0-9]{2}:[0-9]{2}:[0-9]{2}).pickle', f)[1]
    #                    for f in data_list if f.endswith('.pickle')]
    # most_recent_date = max([datetime.strptime(d, '%Y%m%dT%H:%M:%S') for d in file_dates_only]).strftime(
    #     '%Y%m%dT%H:%M:%S')
    # most_recent_file = f"craigslist_{most_recent_date}.pickle"
    # df_listings = pd.read_pickle(os.path.join(module_path, most_recent_file))

    df_listings = df_listings[[col for col in df_listings.columns if 'Unnamed' not in col]]
    df_listings.loc[:, 'result_price'] = df_listings.loc[:, 'result_price'].apply(
        lambda x: x.replace('$', '').replace(',', '') if x is not None else x).astype(float)
    df_listings = df_listings[df_listings.apply(lambda row: 100 < row['result_price'] < 3000, axis=1)]

    for row in df_listings.itertuples():
        ms = ModelSpecs(row)
        rowIdx, model_name, capacity, color = ms.get_specs()
        if rowIdx is None:
            continue
        dq = DatabaseQuery(row)
        hood_id = dq.get_hood()
        query_id = dq.get_query()
        product_id = rowIdx

        cur.execute(f"""SELECT * FROM listing
            WHERE hood_id={hood_id}  
            AND query_id={query_id} 
            AND product_id={product_id} 
            AND result_link='{row.result_link}' 
        """)
        res = cur.fetchall()
        if len(res) > 0:
            logger.debug('file already exists')
            continue

        try:
            cur.execute(
                f"""
                INSERT INTO listing
                VALUES (
                     DEFAULT,
                     {hood_id},
                     {query_id},
                     {product_id},
                    '{datetime.today().strftime('%Y%m%dT%H:%M:%S')}',
                    '{row.result_title}',
                    '{row.result_date}',
                     {row.result_price},
                    '{str(row.result_link).strip()}',
                     {row.map_data_accuracy},
                     {row.map_data_longitude},
                     {row.map_data_latitude},
                    '{str(row.main_img_url).strip()}',
                    '{re.sub(r"'", "", row.posting_body.strip())}',
                    '{str(row.user_notices).replace("'", "''").strip()}',
                    '{row.postingdate}',
                    '{str(row.condition).strip()}'
                )
            """)
            con.commit()
        except Exception as e:
            logger.error(traceback.print_exc())
            continue
        # cur.execute(f"SELECT post_id from listing ORDER BY _last_updated DESC")
        # inserted_id = cur.fetchone()[0]
        inserted_id = cur.lastrowid
        logger.info(f"""Successfully inserted listing post_id: {inserted_id}""")


class ModelSpecs:
    def __init__(self, row):
        self.row = row
        self.color = None
        self.capacity = None
        self.model_name = None
        self.result_title = self.row.result_title
        self.posting_body = self.row.posting_body
        self.search_query = row._2
        self.match_idx = None

    def get_model_name(self):
        ## get original model names
        cur.execute(f"SELECT DISTINCT model_name FROM product_orig")
        current_model_names = cur.fetchall()
        if current_model_names is not None: current_model_names = [x[0] for x in current_model_names]

        ## query from tresult title, ge the best match of the product
        model_name = re.search(rf'{self.search_query.replace(" ", " ?")}', self.result_title, flags=re.IGNORECASE)
        if model_name is not None:
            model_name = difflib.get_close_matches(model_name[0].capitalize(), current_model_names)
            if len(model_name) != 0: model_name = model_name[0]
            else: model_name = None
        self.model_name = model_name

    def get_capacity(self):
        if self.model_name is None:
            return
        cur.execute(f"SELECT DISTINCT capacity FROM product WHERE model_name='{self.model_name}'")
        current_capacities = cur.fetchall()
        if current_capacities is not None: current_capacities = [x[0] for x in current_capacities]
        ## Search for GB or TB from the listing title
        capacity = re.search(r'([0-9 ]{2,4})gb|(1) ?tb', self.result_title, flags=re.IGNORECASE)
        if capacity is None:
            ## If not found from the title, search for GB or TB from the listing body
            capacity = re.search(r'([0-9 ]{2,4})gb|(1) ?tb', self.posting_body, flags=re.IGNORECASE)
        if capacity is not None:
            capacity = difflib.get_close_matches(capacity[0], current_capacities)
            if len(capacity) != 0: capacity = capacity[0]
            else: capacity = None
        # if capacity is not None: capacity = capacity[0].replace(' ', '').strip().upper()
        self.capacity = capacity

    def get_color(self):
        if self.model_name is None:
            return
        ## get model colors from original list
        cur.execute(f"SELECT color FROM product_orig WHERE model_name='{self.search_query}'")
        model_colors = cur.fetchall()
        if model_colors is not None: model_colors = model_colors[0][0].split(', ')

        #Search for the model colors from the listing title
        color = re.search(rf'{"|".join([c.replace(" ", " ?") for c in model_colors])}', self.result_title, flags=re.IGNORECASE)
        if color is None:
            color = re.search(rf'{"|".join([c.replace(" ", " ?") for c in model_colors])}', self.posting_body, flags=re.IGNORECASE)
        if color is not None:
            color = difflib.get_close_matches(color[0].upper(), model_colors)
            if len(color) != 0: color = color[0]
            else: color = None
        self.color = color

    def match_specs(self):
        if self.model_name is None:
            return
        ## TODO: add 'others' value for capacity and color for those listings without color or capacity or both.
        cur.execute(
            f"SELECT * FROM product "
            f"WHERE model_name='{self.model_name}' "
            f"AND capacity='{self.capacity}' "
            f"AND color='{self.color}'")
        match_row = cur.fetchall()
        if len(match_row) != 0:
            match_row = match_row[0][0]
            self.match_idx = match_row

    def get_specs(self):
        self.get_model_name()
        self.get_capacity()
        self.get_color()
        self.match_specs()
        return self.match_idx, self.model_name, self.capacity, self.color


def get_current_models():
    cur.execute('SELECT distinct model_name FROM product WHERE current=1')
    current_models = cur.fetchall()
    current_models = [m[0] for m in current_models]
    current_models_lower = [m[0].lower() for m in current_models]
    return current_models_lower, current_models


if __name__ == '__main__':
    insert_listings()
