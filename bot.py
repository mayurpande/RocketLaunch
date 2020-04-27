import requests
import json
import configparser as cfg


class TelegramBot:

    def __init__(self, config):
        """
        Set token and base url
        :param config:
        """
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):

        """
        Get latest update from user from Bot API
        :param offset: ID of the given offset if there is one
        :return: json content of the response content from the API
        """
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        """
        Uses the Bot API to send a message with params
        :param msg: The actual message itself to send to the User.
        :param chat_id: The current chat id.
        :return: 200 response
        """
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)

        if msg is not None:
            requests.get(url)

    def send_photo(self, chat_id, photo):
        """
        Uses the Bot API to send a photo. Uses post request.
        :param chat_id: The current chat id
        :param photo: The url of the photo
        :return: 200 response
        """
        url = self.base + "sendPhoto?chat_id={}&photo={}".format(chat_id, photo)
        if photo is not None:
            requests.get(url)

    @staticmethod
    def read_token_from_config_file(config):
        """
        Static method to read token from credentials config file.
        :param config: config file
        :return: parsed config
        """
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')
