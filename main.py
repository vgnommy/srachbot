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
        self.offset = 0

    def start_update_in_loop(self, loopTime):
        while True:
            updated_data = self.get_updates()
            print('y', updated_data)
            if updated_data:
                updated_result = updated_data['result']
                self.offset = updated_result[-1]['update_id'] + 1
                print('lastDta', updated_data)
                chat_id = updated_result[-1]['message']['chat']['id']
                print(chat_id)
                send_message_response = self.send_message(chat_id, 'how r u')
            sleep(loopTime)

    def get_updates(self):
        params = {'timeout': 100, 'offset': self.offset}
        response = requests.get(urljoin(self.url, 'getUpdates'), params)
        return response.json()

    def send_message(self, chat, text):
        params = {'chat_id': chat, 'text': text}
        response = requests.post(urljoin(self.url, 'sendMessage'), data=params)
        return response.json()

    def last_update(self, data):
        results = data['result']
        return results


greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.now()

def main():
    greet_bot.start_update_in_loop(30)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

