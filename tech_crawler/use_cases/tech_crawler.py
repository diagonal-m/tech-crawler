from entities.crawling_list import CrawlingList
from entities.site import Site
from entities.news import News

from interfaces.storage import Storage
from interfaces.parameter_store import ParameterStore
from interfaces.notifier import Notifier

class TechCrawler:
  def __init__(self, parameter_store_client: ParameterStore, s3_client: Storage, slack_client: Notifier) -> None:
    self.__parameter_store_client = parameter_store_client
    self.__s3_client = s3_client
    self.__slack_client = slack_client

  def execute(self) -> None:
    crawling_list = CrawlingList(self.__parameter_store_client, self.__s3_client)
    while crawling_list.has_next():
      crawling_target = crawling_list.next()
      site = Site(
        crawling_target,
        self.__parameter_store_client,
        self.__s3_client
      )
      news_list = site.fetch_news()
      for news in news_list:
        self.__slack_client.notify(
          self.__parameter_store_client.params['satoichi_hub_webhook'],
          self.message(news)
        )
        self.__slack_client.notify(
          self.__parameter_store_client.params['satoichi_scrap_webhook'],
          self.message(news)
        )

  def message(self, news: News) -> str:
    return f'{news.site_name}\n<{news.url}|{news.title}>'