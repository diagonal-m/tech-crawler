from typing import List
from news import News

class Site():
  def __init__(self, site_name, url):
    self.site_name = site_name
    self.url = url
    self.latest_html = None
    self.before_html = None
  
  def get_latest_html(self) -> str:
    return ''
  
  def get_before_html(self) -> str:
    return ''
  
  def get_news(self) -> List[News]:
    return []
