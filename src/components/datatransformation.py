from src.logging import logging
from src.exception import CustomException
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact
from src.cosntants import *
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import re
import pandas as pd
import dill
import os
from sklearn.preprocessing import LabelEncoder


# Download only the required resources
nltk.download('punkt')  # For tokenization
nltk.download('wordnet')  # For lemmatization
nltk.download('stopwords')  # For stopwords


class DataTransformation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_transformation_config: DataTransformationConfig):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_transformation_config = data_transformation_config

    @staticmethod
    def read_csv(file_path):
        return pd.read_csv(file_path)

    def start_the_transformation(self):
        try:
            logging.info("Starting the data transformation...")

            # Load train and test data
            train_data = self.read_csv(self.data_ingestion_artifact.train_file_path)
            test_data = self.read_csv(self.data_ingestion_artifact.test_file_path)

            preprocess = Preprocessing()

            # Replace 'text_column' with the actual text column name
            train_data['im getting on borderlands and i will murder you all ,'] = train_data['im getting on borderlands and i will murder you all ,'].map(preprocess.preprocess)
            test_data['im getting on borderlands and i will murder you all ,'] = test_data['im getting on borderlands and i will murder you all ,'].map(preprocess.preprocess)

            # Create directory for transformation object
            os.makedirs(os.path.dirname(self.data_transformation_config.data_transformation_object_dir_path), exist_ok=True)

            # Encode labels
            train_data['Positive'] = preprocess.label_encoder.fit_transform(train_data['Positive'])
            test_data['Positive'] = preprocess.label_encoder.transform(test_data['Positive'])

            # Save the whole Preprocessing object
            preprocessing_object_path = self.data_transformation_config.data_transformation_object_dir_path  # Use directory directly
            with open(preprocessing_object_path, 'wb') as f:
                dill.dump(preprocess, f)

            # Create directory for transformed files
            os.makedirs(os.path.dirname(self.data_transformation_config.data_transformation_train_file), exist_ok=True)

            # Save transformed data
            train_data.to_csv(self.data_transformation_config.data_transformation_train_file, index=False)
            test_data.to_csv(self.data_transformation_config.data_transformation_test_file, index=False)

            logging.info("Data transformation completed successfully.")

            return DataTransformationArtifact(
                self.data_transformation_config.data_transformation_train_file,
                self.data_transformation_config.data_transformation_test_file,
                self.data_transformation_config.data_transformation_object_dir_path
            )

        except Exception as e:
            logging.error(f"Error in data transformation: {e}")
            raise CustomException(e)


class Preprocessing:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.label_encoder = LabelEncoder()

    def preprocess(self, text):
        text = str(text).lower()  # Ensure it's a string and convert to lowercase
        text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
        text = re.sub(r'\d+', '', text)  # Remove numbers
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        tokens = word_tokenize(text)  # Tokenization
        tokens = [word for word in tokens if word not in self.stop_words]  # Remove stopwords
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
        return ' '.join(tokens)

    