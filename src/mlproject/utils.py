import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
# import src.mlproject.utils import read_sql_data
import numpy as np
import pickle

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
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
