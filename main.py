from datetime import datetime
from time import sleep
from urllib.parse import urljoin

import requests

urlTemplate = 'https://api.telegram.org/bot%s/'
token = '1433799498:AAGBMvDz9uUPLb6lOsGzKD_C8wL1bCcL0wg'
url = urlTemplate % token

class BotHandler:
    def __init__(self, token):
        self.url = urlTemplate % token

    def start_update_in_loop(self, loopTime):
        while True:
            updated_data = self.last_update(self.get_updates())
            print(updated_data)
            chat_id = updated_data['message']['chat']['id']
            print(chat_id)
            send_message_response = self.send_message(chat_id, 'how r u')
            sleep(loopTime)

    def get_updates(self):
        params = {'timeout': 100, 'offset': None}
        response = requests.get(urljoin(self.url, 'getUpdates'), params)
        return response.json()

    def send_message(self, chat, text):
        params = {'chat_id': chat, 'text': text}
        response = requests.post(urljoin(self.url, 'sendMessage'), data=params)
        return response.json()

    def last_update(self, data):
        results = data['result']
        return results[-1]


greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.now()

def main():
    greet_bot.start_update_in_loop(60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

