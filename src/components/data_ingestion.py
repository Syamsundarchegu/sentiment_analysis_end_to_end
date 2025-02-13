from src.exception import CustomException
from src.logging import logging
from src.cosntants import *
import os
import sys
from sklearn.model_selection import train_test_split
import pandas as pd
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.data_connection_hub.connection import MongoDBConnection

class DataIngestion():
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
    
    def get_data_from_the_mongodb(self):
        #example uscase 
        try:
            df = MongoDBConnection(database_name,collection_name,mongo_url).connecting_monogo_db()
            
            df = pd.DataFrame(list(df))
            
            df.drop(columns=['_id'],inplace=True,axis=1)
            
            logging.info("sucessfully getting data from the mongodb database...")
        
            os.makedirs(os.path.dirname(self.data_ingestion_config.feature_store_file_path),exist_ok=True)
            logging.info("creating artifact directory..")
            
            df.to_csv(self.data_ingestion_config.feature_store_file_path,header=True,index=False)        
            return df
        except Exception as e:
            raise CustomException(e)
    
    def train_test_split(self,data_frame):
        
        train_file_path = os.path.join(self.data_ingestion_config.data_ingested_train_file_path)
        test_file_path = os.path.join(self.data_ingestion_config.data_ingested_test_file_path)
        
        X,y = train_test_split(data_frame,test_size=train_test_split_ratio,random_state=42)
        logging.info("Splitting data into train and test sets...")
        
        ingested_dir = os.path.dirname(self.data_ingestion_config.data_ingested_test_file_path)
        
        os.makedirs(ingested_dir,exist_ok=True)
        
        X.to_csv(train_file_path,header=True,index=False)
        y.to_csv(test_file_path,header=True,index=False)        
        
        logging.info("Sucessfully split data into train and test sets...")
        logging.info("pushing training and testing data to the ingested directory..")
        
        
    def put_key_to_start_the_data_ingestion(self):
        try:
            logging.info("i am starting the data ingestion...")
            
            dataframe = self.get_data_from_the_mongodb()
            
            self.train_test_split(dataframe)
            
            logging.info("succesfully exist from the data ingestion")
            
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.data_ingested_train_file_path,test_file_path=self.data_ingestion_config.data_ingested_test_file_path)
            
            logging.info(f"Data ingestion artifact : {data_ingestion_artifact}")
            
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e)