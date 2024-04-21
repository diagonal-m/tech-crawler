from entities.crawling_list import CrawlingList
from entities.site import Site

from interfaces.storage import Storage
from interfaces.parameter_store import ParameterStore

class TechCrawler:
  def __init__(self, parameter_store_client: ParameterStore, s3_client: Storage) -> None:
    self.__parameter_store_client = parameter_store_client
    self.__s3_client = s3_client

  def execute(self) -> None:
    crawling_list = CrawlingList(self.__parameter_store_client, self.__s3_client).crawling_list
    for i in range(crawling_list.shape[0]):
      row = crawling_list.iloc[i]
      site = Site(row['site_name'], row['url'])
      print(site.site_name, site.url)