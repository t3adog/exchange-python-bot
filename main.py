from asyncio.log import logger
import logging
from time import sleep
import requests
from exchangelib import Credentials, Account, Message
import config

properties = config.get_properties()
credentials = Credentials(
    properties['exchange']['login'], properties['exchange']['password'])
account = Account(
    properties['exchange']['email'], credentials=credentials, autodiscover=True)
bot_token = str(properties['telegram']['telegram_token'])
bot_chatID = str(properties['telegram']['telegram_chat'])


def telegram_bot_send_text(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def check_nagios():
    logging.info("Check mail")
    
    nagios_dir = account.root / 'implement' / 'your' / 'subdir'
    unread = nagios_dir.filter(is_read=False).order_by('datetime_received')
    for msg in unread[:100]:
        item_body = msg.body
        telegram_bot_send_text(item_body)
        msg.is_read = True
        msg.save()


if __name__ == '__main__':
    config.init()
    while True:
        check_nagios()
        sleep(properties["sleep_time_sec"])
