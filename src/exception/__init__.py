


import sys

def get_error_message(message):
    exc_type, exc_value, exc_traceback = sys.exc_info()

    if exc_traceback is None:
        return f"Error occurred: {message} (No traceback available)"

    error_message = (
        f"Error occurred in file '{exc_traceback.tb_frame.f_code.co_filename}', "
        f"line {exc_traceback.tb_lineno}. Message: {message}"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = get_error_message(message)
    
    def __str__(self):
        return f"Custom Exception: {self.message}"