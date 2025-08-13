#this file, we provide the logging configurations...basically debugging easy karne ke liye and to keep a track sort of
import logging
import os
from datetime import datetime

#structure defination of our logfile
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(), "log_report", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)