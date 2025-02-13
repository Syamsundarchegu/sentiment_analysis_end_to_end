import os
from dataclasses import dataclass
from src.cosntants import  *


class TrainingPipeline:
    artifact_directory_name : str =  artifact_dir_name

training_pipeline = TrainingPipeline
    
    
class DataIngestionConfig:
    data_ingestion_path  = os.path.join(training_pipeline.artifact_directory_name, data_ingestion_dir_name)
    feature_store_file_path = os.path.join(data_ingestion_path, data_ingestion_feature_store_dir_name, raw_file_name)
    data_ingested_train_file_path = os.path.join(data_ingestion_path, data_ingestion_ingested_dir_name,train_file_name)
    data_ingested_test_file_path = os.path.join(data_ingestion_path,data_ingestion_ingested_dir_name,test_file_name)
    train_test_split_ratio_file_path = train_test_split_ratio
    
class DataTransformationConfig:
    data_transformation_dir_path = os.path.join(training_pipeline.artifact_directory_name, data_transformation_dir_name)
    data_transformation_train_file = os.path.join(data_transformation_dir_path,data_transformation_transformed_dir_name,data_transformation_train_file_name)
    data_transformation_test_file = os.path.join(data_transformation_dir_path,data_transformation_transformed_dir_name,data_transformation_test_file_name)
    data_transformation_object_dir_path = os.path.join(data_transformation_dir_path,data_transformation_object_dir_name,data_transformation_object_file_name)

class ModelConfig:
    model_dir_path = os.path.join(training_pipeline.artifact_directory_name, best_model_directory, best_model_name)