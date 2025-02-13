

train_file_name : str = "train.csv"
test_file_name  : str = "test.csv"
raw_file_name : str = "raw.csv"

train_test_split_ratio : float = 0.20

database_name : str = "twitter"

collection_name : str = "tweets"

mongo_url :str = "mongodb+srv://syamsundar:syam@cluster0.tai4x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    

artifact_dir_name : str = "artifact"

pipeline_name  : str = "twitter"

data_ingestion_dir_name : str = "data_ingestion"
data_ingestion_ingested_dir_name : str = "ingested"
data_ingestion_feature_store_dir_name : str = "feature_store"


data_transformation_dir_name : str = "data_transformation"
data_transformation_transformed_dir_name : str = "transformed"
data_transformation_object_file_name : str = "preprocessing.pkl"
data_transformation_train_file_name : str =  "transformed_train.csv"
data_transformation_test_file_name : str =  "transformed_test.csv"
data_transformation_object_dir_name : str = "transformed_object"


best_model_directory : str = "best_model_directory"
best_model_name : str = "best_model.pkl"