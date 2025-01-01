import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
# import src.mlproject.utils import read_sql_data

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("reading SQL database started")
    try:
        mydb = pymysql.connect( 
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info(f"Connection established: {mydb}")
        df = pd.read_sql_query('select * from student',mydb)
        print(df.head())
        
        return df
        
    except Exception as ex:
        raise CustomException(ex)