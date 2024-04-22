from entities.crawling_list import CrawlingList
from entities.site import Site

from interfaces.storage import Storage
from interfaces.parameter_store import ParameterStore

class TechCrawler:
  def __init__(self, parameter_store_client: ParameterStore, s3_client: Storage) -> None:
    self.__parameter_store_client = parameter_store_client
    self.__s3_client = s3_client

  def execute(self) -> None:
    crawling_list = CrawlingList(self.__parameter_store_client, self.__s3_client)
    while crawling_list.has_next():
      crawling_target = crawling_list.next()
      site = Site(crawling_target['site_name'], crawling_target['url'])
      print(site.site_name, site.url)