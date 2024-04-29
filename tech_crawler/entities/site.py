from urllib.parse import urlparse, ParseResult
from typing import List

import requests

from interfaces.parameter_store import ParameterStore
from interfaces.storage import Storage

from entities.news import News

import pandas as pd
from bs4 import BeautifulSoup

class Site():
  def __init__(self, crawling_target: pd.Series, parameter_store: ParameterStore, storage: Storage):
    self.site_name = crawling_target['site_name']
    self.url = crawling_target['url']
    self.area_tag = crawling_target['area_tag']
    self.area_params = {crawling_target['area_attr_type']: crawling_target['area_attr_name']}
    self.a_params = {crawling_target['a_attr_type']: crawling_target['a_attr_name']}
    self.__parameter_store = parameter_store
    self.__storage = storage
    self.__key = self.__make_key()
  
  def fetch_news(self) -> List[News]:
    latest_html = self.get_latest_html()
    before_html = self.get_before_html()

    # クローリング初回の場合
    if not before_html:
      self.__storage.upload(self.__parameter_store.params['urls_bucket_name'], self.__key, latest_html)
      return []

    latest_a_tags = self.parse_anchor_tags(latest_html)
    before_a_tags = self.parse_anchor_tags(before_html)

    new_a_tags = self.get_new_a_tags(latest_a_tags, before_a_tags)
    if len(new_a_tags) == 0:
      return []

    self.__storage.upload(self.__parameter_store.params['urls_bucket_name'], self.__key, latest_html)

    news_list = self.make_news(new_a_tags)

    return news_list
  
  def get_latest_html(self) -> None:
    """
    サイトの最新HTMLを取得
    """
    response = requests.get(self.url)
    response.raise_for_status()
    return response.text
  
  def get_before_html(self) -> bool:
    """
    サイトの前回クローリング時のHTMLを取得
    """
    return self.__storage.download_file(
      self.__parameter_store.params['urls_bucket_name'],
      self.__key
    )

  def get_new_a_tags(self, latest_a_tags, before_a_tags) -> list:
    """
    差分を取得するメソッド
    """
    before_hrefs = [a_tag.get('href') for a_tag in before_a_tags]
    
    return [a_tag for a_tag in latest_a_tags if a_tag.get('href') not in before_hrefs]
  
  def parse_anchor_tags(self, html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')

    if self.area_tag:
      soup = soup.find(self.area_tag, **self.area_params)

    return [a_tag for a_tag in soup.find_all('a', **self.a_params) if a_tag.has_attr('href')]
  
  def make_news(self, new_a_tags: list) -> List[News]:
    news_list = []
    for new_a_tag in new_a_tags:
      news_list.append(News(
        self.site_name,
        new_a_tag.get_text(),
        self.url,
        new_a_tag.get('href')
      ))
    return news_list

  def __make_key(self) -> str:
    """
    S3へのパスを生成するメソッド
    """
    # ParseResult(scheme='https', netloc='www.xxxx.com', path='/', params='', query='', fragment='')
    parsed_url: ParseResult = urlparse(self.url)
    return '/'.join([
      part.strip('/') for part in list(parsed_url) if part or part == '/'
    ])
