import logging
import os
from datetime import datetime
# import sys
# from logging import StreamHandler, FileHandler, Formatter
# from logging.handlers import TimedRotatingFileHandler
# from typing import Optional
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

if __name__ == "__main__":
    logging.info("Logging is set up and ready to use.")
    # logging.debug("This is a debug message.")
    # logging.warning("This is a warning message.")
    # logging.error("This is an error message.")
    # logging.critical("This is a critical message.")