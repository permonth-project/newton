from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, engine
import uvicorn
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://newton.permonth.tech",
    "http://permonth.tech"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/get-all")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_prices = crud.get_all_prices(db, skip=skip, limit=limit)
    # all_prices = list(all_prices)
    # all_prices = pd.DataFrame(all_prices).to_dict(orient="list")

    return all_prices


@app.get("/api/get-avg-single")
def read_users(product_id: str = '', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avg_prices = crud.get_avg_prices_single(product_id, db, skip=skip, limit=limit)

    return avg_prices


@app.get("/api/get-avg-multiple")
def read_users(product_id: str = '', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avg_prices = crud.get_avg_prices_multiple(
        product_id, db, skip=skip, limit=limit)

    return avg_prices


@app.get("/api/get-products")
def read_products(product_id: str = '', model: str = '', capacity: str = '', color: str = '', current: int = 0, skip: int = 0, db: Session = Depends(get_db)):
    products = crud.get_product_details(
        product_id, model, capacity, color, current, db)

    return products


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
