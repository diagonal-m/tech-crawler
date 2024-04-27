from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, webhook: str, message: str) -> None:
        pass
