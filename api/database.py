from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPORT = os.getenv('DBPORT')
DBPASSWORD = os.getenv('DBPASSWORD')
DATABASE = os.getenv('DATABASE')

engine = create_engine(f'mysql+pymysql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DATABASE}', echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
