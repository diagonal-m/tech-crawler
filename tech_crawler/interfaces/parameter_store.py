from abc import ABC, abstractmethod

class ParameterStore(ABC):
    @abstractmethod
    def params(self) -> dict:
        pass
