import json
import requests

from interfaces.notifier import Notifier

class SlackClient(Notifier):
    def __init__(self) -> None:
        pass

    def notify(self, webhook: str, message: str) -> None:
        """
        スラックにメッセージを送信
        """
        requests.post(webhook, data=json.dumps({
            "text": message
        }))
