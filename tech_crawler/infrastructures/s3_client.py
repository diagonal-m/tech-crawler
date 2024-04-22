from io import StringIO

import pandas as pd
import boto3

from interfaces.storage import Storage

class S3Client(Storage):
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def download_csv(self, bucket_name: str, key: str) -> pd.DataFrame:
        response = self.s3_client.get_object(
            Bucket=bucket_name,
            Key=key
        )
        # レスポンスの本文（body）からCSVファイルの内容を取得
        csv_string = response['Body'].read().decode('utf-8')
        # 文字列データから直接pandasのデータフレームを作成
        df = pd.read_csv(StringIO(csv_string))
        return df

    def upload(self, key, data):
        print(f"Uploading {key} to S3 bucket {self.bucket_name}")
        # Code to upload file to S3