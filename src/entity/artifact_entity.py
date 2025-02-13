from dataclasses import dataclass


@dataclass

class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str
    
    
@dataclass
class DataTransformationArtifact:
    train_transformed_file_path:str
    test_transformed_file_path:str
    transformed_object_file_path:str
    
@dataclass
class TrainingArtifact:
    best_model_file_path:str