import logging
from logging import handlers
import configparser

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logHandler = handlers.TimedRotatingFileHandler('log/bot.log', when='D', interval=1)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")

logHandler.setFormatter(formatter)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

properties = configparser.ConfigParser()
properties.sections()
properties.read('config/config.ini')
