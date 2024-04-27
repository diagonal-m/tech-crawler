from interfaces.parameter_store import ParameterStore
import boto3


class ParameterStoreClient(ParameterStore):
    def __init__(self):
        self.params = self.params()

    def params(self):
        return {
            'crawling_master_file_name': 'crawling_master.csv',
            'crawling_master_bucket_name': self._get_parameter('crawling-master-bucket-name'),
            'urls_bucket_name': self._get_parameter('urls-bucket-name'),
            'satoichi_hub_webhook': self._get_parameter('satoichi-hub-tech-news-webhook'),
        }

    def _get_parameter(self, name: str) -> str:
        ssm = boto3.client('ssm')
        return ssm.get_parameter(Name=name, WithDecryption=True)['Parameter']['Value']
