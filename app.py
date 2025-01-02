from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.data_transformation import DataTransformation

import sys


if __name__ == "__main__":
    logging.info("the execution has started ")
    
    try :
        # data_ingestion_config = DataIngestionConfig()
        logging.info("Starting Data Ingestion...")
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed: Train - {train_data_path}, Test - {test_data_path}")
        
        # data_transformation_config = DataTransformationConfig()
        logging.info("Starting Data Transformation...")
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        logging.info(f"Data Transformation completed: Preprocessor saved at {preprocessor_path}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e,sys)