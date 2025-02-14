import dill

class TestingParameter:
    def __init__(self, comment):
        self.comment = comment  # Store user input

    def predict(self):
        preprocessor_path = r"C:\Users\syamc\OneDrive\Desktop\nlp_project_end_to_end\artifact\data_transformation\transformed_object\preprocessing.pkl"
        model_path = r"C:\Users\syamc\OneDrive\Desktop\nlp_project_end_to_end\artifact\best_model_directory\best_model.pkl"

        try:
            # Load the preprocessor
            with open(preprocessor_path, 'rb') as f:
                preprocessor = dill.load(f)

            # Apply preprocessing to the input comment
            transformed_comment = preprocessor.preprocess([self.comment])  # Ensure preprocessor supports this
            print(transformed_comment)
            # Load the model
            with open(model_path, 'rb') as f:
                model = dill.load(f)

            # Make a prediction
            prediction = model.predict(transformed_comment)  # Model expects transformed input

            return prediction, transformed_comment # Convert to string for Flask response

        except Exception as e:
            return f"Error: {str(e)}"

