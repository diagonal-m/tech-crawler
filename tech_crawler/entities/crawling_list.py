import pandas as pd

from interfaces.parameter_store import ParameterStore
from interfaces.storage import Storage

class CrawlingList():
  def __init__(self, parameter_store: ParameterStore, storage: Storage):
    self.__parameter_store = parameter_store
    self.__storage = storage
    self.__crawling_list = self.__get_crawling_list()
    self.__index = 0

  def next(self) -> pd.Series:
    crawling_target = self.__crawling_list.iloc[self.__index]
    self.__index += 1

    return crawling_target

  def has_next(self) -> bool:
    return self.__crawling_list.shape[0] > self.__index

  def __get_crawling_list(self) -> pd.DataFrame:
    return self.__storage.download_csv(
      self.__parameter_store.params['crawling_master_bucket_name'],
      self.__parameter_store.params['crawling_master_file_name']
    )