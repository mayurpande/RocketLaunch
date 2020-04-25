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


def display_content(chat_id, message):
    """
    call generate_img fn and get frame id, call send_photo fn, call send_message fn
    :param chat_id: chat id from the bot
    :param message: message from user
    :return: frame id
    """
    photo_url, frame = generate_img()
    bot_ob.send_photo(chat_id, photo_url)
    reply = make_reply(message, frame)
    bot_ob.send_message(reply, chat_id)
    return frame


def handle_start_command():
    """
    Telegram Bot only allows the bot to start with a special in-built command '/start'. In order to send messages to the
    bot the chat_id is needed, in order to get the latest update the update_id is needed.
    :return: chat_id, update_id, message
    """
    update_id = None
    chat_id = None

    true_if_message_not_start = True
    while true_if_message_not_start is True:
        updates = bot_ob.get_updates(update_id)
        updates = updates["result"]
        if updates:
            for item in updates:
                update_id = item["update_id"]
                try:
                    message = str(item["message"]["text"])
                except:
                    message = None
                chat_id = item["message"]["from"]["id"]
                if '/start' in message:
                    bot_ob.send_message('Starting a new game', chat_id)
                    true_if_message_not_start = False
                else:
                    bot_ob.send_message('Command not detected to start a game type /start', chat_id)

    return update_id, chat_id, message


def bisect_algorithm(bi_sected_list, frame):
    """
    Bisection (left) algorithm to sort
    :param bi_sected_list:
    :param frame:
    :return:
    """
    inc = 0
    bi_len = len(bi_sected_list)

    while inc < bi_len:
        mid_range = (inc + bi_len) // 2
        if bi_sected_list[mid_range] < frame:
            inc = mid_range + 1
        else:
            bi_len = mid_range

    bi_sected_list.insert(inc, frame)

    return bi_sected_list