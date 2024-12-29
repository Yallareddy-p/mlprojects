# logger.py file
import logging
import os
from datetime import datetime

LOG_FILE=f"{os.path.dirname(os.path.abspath(__file__))}/logs/{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path=os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.error(f"Exception occured: {e}")
        logging.error(f"Exception occured: {e}", exc_info=True)

logging.info('This is an info message')
logging.debug('This is a debug message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.critical('This is a critical message')

