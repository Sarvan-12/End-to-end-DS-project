from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainerConfig,ModelTrainer

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
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        # logging.info(f"Data Transformation completed: Preprocessor saved at {preprocessor_path}")
        
        #model training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e,sys)