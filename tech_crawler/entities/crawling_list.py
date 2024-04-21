import pandas as pd

from interfaces.parameter_store import ParameterStore
from interfaces.storage import Storage

class CrawlingList():
  def __init__(self, parameter_store: ParameterStore, storage: Storage):
    self.__parameter_store = parameter_store
    self.__storage = storage
    self.crawling_list = self.get_crawling_list()

  def get_crawling_list(self) -> pd.DataFrame:
    return self.__storage.download_csv(
      self.__parameter_store.params['crawling_master_bucket_name'],
      self.__parameter_store.params['crawling_master_file_name']
    )