from urllib.parse import urljoin

class News():
  def __init__(self, site_name: str, title: str, site_url: str, href: str):
    self.site_name = site_name
    self.title = title
    self.url = urljoin(site_url, href)
