from interfaces.notifier import Notifier

class SlackClient(Notifier):
    def __init__(self) -> None:
        super().__init__()

    def notify(self, message: str) -> None:
        print(message)
