import os
import dill
import pandas as pd
from pycaret.classification import *
from src.entity.artifact_entity import DataTransformationArtifact, TrainingArtifact
from src.entity.config_entity import ModelConfig
from src.exception import CustomException
from src.logging import logging

class ModelTraining:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact, model_config: ModelConfig):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_config = model_config

    @staticmethod
    def read_csv(filename):
        """Reads a CSV file and returns a DataFrame."""
        return pd.read_csv(filename)
    
    def train_the_model(self):
        """Trains the model using PyCaret, tunes it, saves it, and returns ModelTrainingArtifact."""
        try:
            logging.info("Reading training data...")
            train_file = self.read_csv(self.data_transformation_artifact.train_transformed_file_path)
            
            # Renaming and dropping unnecessary columns
            train_file.rename(columns={'Positive': 'Target', 'im getting on borderlands and i will murder you all ,': 'Comments'}, inplace=True)
            train_file.drop(columns=['2401', 'Borderlands'], inplace=True)

            logging.info("Initializing PyCaret setup...")
            clf_setup = setup(train_file, target='Target', session_id=42)

            logging.info("Comparing models to find the best one...")
            best_model = compare_models()

            logging.info(f"Best model selected: {best_model}")

            # logging.info("Performing hyperparameter tuning on the best model...")
            # tuned_model = tune_model(best_model)

            logging.info("Saving the trained model...")
            os.makedirs(os.path.dirname(self.model_config.model_dir_path), exist_ok=True)
            with open(self.model_config.model_dir_path, 'wb') as f:
                dill.dump(best_model, f)

            logging.info(f"Model saved successfully at {self.model_config.model_dir_path}")

            # ✅ Return ModelTrainingArtifact with the best model path
            return TrainingArtifact(self.model_config.model_dir_path)

        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise CustomException(e)
        
    def start_the_model_training(self):
        """Starts the model training pipeline and returns the ModelTrainingArtifact."""
        return self.train_the_model()
