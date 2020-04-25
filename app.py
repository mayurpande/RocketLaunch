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


def generate_img():
    """
    Generate a random number between 1 - 616196 and append to url to get frame
    :return: String var URL to get frame of video
    """
    frame_rand = randint(1, 61696)
    url = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(' \
          'Hosted%20Webcast)-wbSwFU6tY1c/frame/' + str(frame_rand)
    return url, frame_rand


def make_reply(msg, frame):
    """
    Returns response to send to the User
    :param msg: message var from user
    :param frame: frame id
    :return: string var with frame id in it
    """
    reply = None
    if msg is not None:
        reply = str(frame) + ' - has the rocket launched yet? (y/n)'
    return reply
