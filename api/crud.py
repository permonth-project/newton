from sqlalchemy.orm import Session
import pandas as pd


def get_all_prices(db: Session, skip: int = 0, limit: int = 100):
    ## get prices for each listing on the enrtire database
    res = db.execute(f"""
        SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
        FROM (SELECT post_id, result_price, product_id FROM mydb.listing) as listing, 
        (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
        WHERE listing.product_id=product.id 
        AND product.current_=1;
    """)

    df = pd.DataFrame(list(res))
    return df.set_index('post_id').to_dict(orient='index')


def get_avg_prices(product_id: int, db: Session, skip: int = 0, limit: int = 100):
    ## get prices for each listing on the enrtire database
    if product_id > 0:
        res = db.execute(f"""
            SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
            FROM (SELECT post_id, postingdate, result_price, product_id FROM mydb.listing) as listing, 
            (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
            WHERE listing.product_id=product.id 
            AND listing.product_id={product_id}
            AND product.current_=1;
        """)
    else:
        res = db.execute(f"""
            SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
            FROM (SELECT post_id, postingdate, result_price, product_id FROM mydb.listing) as listing, 
            (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
            WHERE listing.product_id=product.id 
            AND product.current_=1;
        """)

    df = pd.DataFrame(list(res))
    df['result_date_onlydate'] = pd.to_datetime(df['postingdate'].str[:19], format='%Y-%m-%dT%H:%M:%S').dt.date

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

