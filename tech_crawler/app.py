from use_cases.tech_crawler import TechCrawler

from infrastructures.parameter_store_client import ParameterStoreClient
from infrastructures.s3_client import S3Client

def lambda_handler(event, context):
    print('start')
    tech_crawler = TechCrawler(ParameterStoreClient(), S3Client())
    tech_crawler.execute()
    print('end')
