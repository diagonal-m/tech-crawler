from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def download(self, key: str) -> None:
        pass
    
    @abstractmethod
    def upload(self, key: str, data: str) -> None:
        pass
