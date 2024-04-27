from use_cases.tech_crawler import TechCrawler

from infrastructures.parameter_store_client import ParameterStoreClient
from infrastructures.s3_client import S3Client
from infrastructures.slack_client import SlackClient

def lambda_handler(event, context):
    print('start')
    tech_crawler = TechCrawler(ParameterStoreClient(), S3Client(), SlackClient())
    tech_crawler.execute()
    print('end')
