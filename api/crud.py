from sqlalchemy.orm import Session
#import models
import pandas as pd


def get_prices(db: Session, skip: int = 0, limit: int = 100):
    # db.execute()
    return db.query(models.Listing).limit(limit).all()


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



def get_avg_prices(db: Session, skip: int = 0, limit: int = 100):
    ## get prices for each listing on the enrtire database
    res = db.execute(f"""
        SELECT listing.*, product.model_name, product.color, product.capacity, product.current_  
        FROM (SELECT post_id, result_date, result_price, product_id FROM mydb.listing) as listing, 
        (SELECT id, model_name, color, capacity, current_ FROM mydb.product) as product 
        WHERE listing.product_id=product.id 
        AND product.current_=1;
    """)

    df = pd.DataFrame(list(res))

    df_res = pd.DataFrame()
    df_group = df[['product_id', 'result_price', 'model_name', 'capacity', 'color']].astype(
        {'product_id': int, 'result_price': float}).groupby(by=['product_id', 'model_name', 'capacity', 'color'])
    df_res.loc[:, 'price_avg'] = df_group.mean()
    df_res.loc[:, 'price_high'] = df_group.max()
    df_res.loc[:, 'price_low'] = df_group.min()
    df_res = df_res.reset_index()

    return df_res.to_dict(orient='records')

