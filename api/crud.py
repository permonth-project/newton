from sqlalchemy.orm import Session
import pandas as pd
from sqlalchemy.sql import text


def get_all_prices(db: Session, skip: int = 0, limit: int = 100):
    # get prices for each listing on the enrtire database
    res = db.execute(text(f"""
        SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
        FROM (SELECT post_id, result_price, product_id FROM mydb.listing) as listing, 
        (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
        WHERE listing.product_id=product.id 
        AND product.current_=1;
    """))

    df = pd.DataFrame(list(res))
    return df.set_index('post_id').to_dict(orient='index')


def get_avg_prices_single(product_id: int, db: Session, skip: int = 0, limit: int = 100):
    # get prices for a single listing from the database
    if product_id > 0:
        res = db.execute(text(f"""
            SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
            FROM (SELECT post_id, postingdate, result_price, product_id FROM mydb.listing) as listing, 
            (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
            WHERE listing.product_id=product.id 
            AND listing.product_id in ({product_id})
            AND product.current_=1;
        """))
    else:
        res = db.execute(text(f"""
            SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
            FROM (SELECT post_id, postingdate, result_price, product_id FROM mydb.listing) as listing, 
            (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
            WHERE listing.product_id=product.id 
            AND product.current_=1;
        """))

    df = pd.DataFrame(list(res))
    if df.empty:
        return None

    df['result_date_onlydate'] = pd.to_datetime(
        df['postingdate'].str[:19], format='%Y-%m-%dT%H:%M:%S').dt.date

    df_res = pd.DataFrame()
    df_group = df[['result_date_onlydate', 'product_id', 'result_price', 'model_name', 'capacity', 'color']]\
        .astype({'product_id': int, 'result_price': float})\
        .groupby(by=['product_id', 'result_date_onlydate', 'model_name', 'capacity', 'color'])
    df_res.loc[:, 'price_avg'] = df_group.mean()
    df_res.loc[:, 'price_high'] = df_group.max()
    df_res.loc[:, 'price_low'] = df_group.min()
    df_res = df_res.reset_index()

    return df_res.to_dict(orient='records')
    # return df_res.groupby('product_id')[['result_date_onlydate', 'price_avg', 'price_high', 'price_low']].apply(dict).to_dict()


def get_avg_prices_multiple(product_id: str, db: Session, skip: int = 0, limit: int = 100):
    # get prices of multiple product_id from the database
    product_id_list = product_id.split(',')
    if product_id != '':
        res = db.execute(text(f"""
            SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
            FROM (SELECT post_id, postingdate, result_price, product_id FROM mydb.listing) as listing, 
            (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
            WHERE listing.product_id=product.id 
            AND listing.product_id in ({product_id})
            AND product.current_=1;
        """))
    else:
        res = db.execute(text(f"""
            SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
            FROM (SELECT post_id, postingdate, result_price, product_id FROM mydb.listing) as listing, 
            (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
            WHERE listing.product_id=product.id 
            AND product.current_=1;
        """))

    df = pd.DataFrame(list(res))
    if df.empty:
        return None

    # Find unique columns out of "product_id" and "model_name"
    product_id_unique = df['product_id'].unique()
    model_name_unique = df['model_name'].unique()
    color_unique = df['color'].unique()
    capacity_unique = df['capacity'].unique()
    group_id = ''
    if product_id_unique.shape[0] == 1:
        group_id = product_id_unique[0]
    elif model_name_unique.shape[0] == 1:
        if capacity_unique.shape[0] == 1:
            group_id = f"{model_name_unique[0]} {capacity_unique[0]}"
        elif color_unique.shape[0] == 1:
            group_id = f"{model_name_unique[0]} {color_unique[0]}"
        else:
            group_id = model_name_unique[0]

    df = df[['postingdate', 'result_price']]
    df['group_id'] = group_id
    df['result_date_onlydate'] = pd.to_datetime(
        df['postingdate'].str[:19], format='%Y-%m-%dT%H:%M:%S').dt.date

    df_res = pd.DataFrame()
    df_group = df[['result_date_onlydate', 'group_id', 'result_price']]\
        .astype({'group_id': str, 'result_price': float})\
        .groupby(by=['group_id', 'result_date_onlydate'])
    df_res.loc[:, 'price_avg'] = df_group.mean()
    df_res.loc[:, 'price_high'] = df_group.max()
    df_res.loc[:, 'price_low'] = df_group.min()
    df_res = df_res.reset_index()

    return df_res.to_dict(orient='records')
    # return df_res.groupby('product_id')[['result_date_onlydate', 'price_avg', 'price_high', 'price_low']].apply(dict).to_dict()


def get_product_details(product_id, model, capacity, color, current, db: Session, skip: int = 0, limit: int = 100):
    product_query = ''
    model_query = ''
    capacity_query = ''
    color_query = ''
    current_query = ''
    if product_id != '':
        product_query = f"AND id in ({product_id})"
    if model != '':
        model_query = f"AND model_name='{model}'"
    if capacity != '':
        capacity_query = f"AND capacity='{capacity}'"
    if color != '':
        color_query = f"AND color='{color}'"
    if current != 0:
        current_query = f"AND current_='{current}'"

    query = f"""
        SELECT * FROM mydb.product 
        WHERE 1
        {product_query} 
        {model_query} 
        {capacity_query} 
        {color_query} 
        {current_query}
    """

    res = db.execute(text(query))
    df = pd.DataFrame(list(res))

    return df.to_dict(orient='records')
