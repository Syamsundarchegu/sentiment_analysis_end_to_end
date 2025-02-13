import sys
from src.exception import CustomException
from src.logging import logging
from src.components.data_ingestion import DataIngestion
from src.components.datatransformation import DataTransformation
from src.components.model_trainer import ModelTraining
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelConfig
from src.entity.artifact_entity import DataTransformationArtifact, TrainingArtifact, DataIngestionArtifact

# ✅ **Main execution starts here**
if __name__ == '__main__':
    try:
        logging.info("🚀 Starting Data Ingestion...")

        # **Step 1: Data Ingestion**
        ingestion_obj = DataIngestion(DataIngestionConfig())
        data_ingestion_artifact = ingestion_obj.put_key_to_start_the_data_ingestion()
        
        logging.info("✅ Data Ingestion completed successfully.")

        logging.info("🚀 Starting Data Transformation...")

        # **Step 2: Data Transformation**
        transformation_obj = DataTransformation(
            data_ingestion_artifact=data_ingestion_artifact, 
            data_transformation_config=DataTransformationConfig()
        )
        data_transformation_artifact = transformation_obj.start_the_transformation()
        
        logging.info("✅ Data Transformation completed successfully.")

        logging.info("🚀 Starting Model Training...")

        # **Step 3: Model Training**
        model_trainer_obj = ModelTraining(
            data_transformation_artifact=data_transformation_artifact, 
            model_config=ModelConfig()
        )
        model_training_artifact = model_trainer_obj.start_the_model_training()

        logging.info(f"✅ Model Training completed successfully. Best model saved at: {model_training_artifact.best_model_file_path}")

    except Exception as e:
        logging.error(f"❌ An error occurred: {e}")
        raise CustomException(e)
