from bot import TelegramBot
from random import randint

bot_ob = TelegramBot("config.cfg")


def check_message_contents(msg):
    """
    Determines if the message variable is correct response
    :param msg:
    :return: String var ok or Prompt response
    """
    if msg == "y" or msg == "n":
        return 'ok'
    else:
        return 'Response needs to be either "y" or "n"'


