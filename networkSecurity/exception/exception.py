import sys
from networkSecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message=error_message
        _, _, exc_tb=error_details.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return 'error in python script named [{0}] at line [{1}], error_desc: [{2}]'.format(
        self.file_name, self.lineno, str(self.error_message))

