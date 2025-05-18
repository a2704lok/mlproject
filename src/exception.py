import sys

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details as input and returns a formatted string
    containing the error message and the line number where the error occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It overrides the __init__ method to provide a custom error message.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message