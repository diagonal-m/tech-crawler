from interfaces.storage import Storage
from interfaces.notifier import Notifier
from interfaces.parameter_store import ParameterStore

class TechCrawler:
  def __init__(self, s3_client: Storage, slack_client: Notifier, parameter_store_client: ParameterStore) -> None:
    self.s3_client = s3_client
    self.slack_client = slack_client
    self.parameter_store_client = parameter_store_client

  def execute(self) -> None:
    print('クローリングスタート')
