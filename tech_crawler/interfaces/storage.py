from abc import ABC, abstractmethod
import pandas as pd

class Storage(ABC):
    @abstractmethod
    def download_csv(self, bucket_name: str, key: str) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def upload(self, bucket_name: str, key: str, data: str) -> None:
        pass
