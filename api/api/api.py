import logging
from logging.handlers import RotatingFileHandler

import threading
import requests

from datetime import datetime

from . import create_app

# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
file = RotatingFileHandler('api.log', maxBytes=2000, backupCount=10)
file.setFormatter(formatter)
# Set log level and add handlers
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)
logger.addHandler(file)

api = create_app()


if __name__ == '__main__':
    api.run()
