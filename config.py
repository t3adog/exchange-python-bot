import logging
from logging import handlers
import yaml


logger = logging.getLogger()
logger.setLevel(logging.INFO)

logHandler = handlers.TimedRotatingFileHandler('log/bot.log', when='D', interval=1)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")

logHandler.setFormatter(formatter)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

def get_properties() -> dict:
    with open("config/application.yml", "r") as stream:
        properties = yaml.safe_load(stream)
        return properties

def init():
    logger.info(" ___      __                  __   ___     __      ___       __           __   __  ___ ")
    logger.info("|__  \_/ /  ` |__|  /\  |\ | / _` |__  __ |__) \ /  |  |__| /  \ |\ | __ |__) /  \  |  ")
    logger.info("|___ / \ \__, |  | /~~\ | \| \__> |___    |     |   |  |  | \__/ | \|    |__) \__/  |  ")
    logger.info("                                                                                       ")
    logger.info("Bot init...                                                                            ")