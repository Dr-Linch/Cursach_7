from django.conf import settings
import requests


class TgBot:
    """
    Класс для отправки сообщений в Телеграм бот
    """
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_BOT_API_KEY

    def send_message(self, text, chat_id):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )