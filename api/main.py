from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, engine
import uvicorn
import pandas as pd


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get-all/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_prices = crud.get_all_prices(db, skip=skip, limit=limit)
    # all_prices = list(all_prices)
    # all_prices = pd.DataFrame(all_prices).to_dict(orient="list")

    return all_prices


@app.get("/get-avg/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avg_prices = crud.get_avg_prices(db, skip=skip, limit=limit)

    return avg_prices


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
