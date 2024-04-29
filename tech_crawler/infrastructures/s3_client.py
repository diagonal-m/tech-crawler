from typing import Tuple
from io import StringIO, BytesIO

import pandas as pd
import boto3

from interfaces.storage import Storage

class S3Client(Storage):
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def download_csv(self, bucket_name: str, key: str) -> pd.DataFrame:
        csv_string = self.download_file(bucket_name, key)
        # 文字列データから直接pandasのデータフレームを作成
        df = pd.read_csv(StringIO(csv_string))
        df = df.fillna('')
        return df

    def download_file(self, bucket_name: str, key: str) -> str:
        try:
            response = self.s3_client.get_object(
                Bucket=bucket_name,
                Key=key
            )
            # レスポンスの本文（body）からファイルの内容を取得
            file_content = response['Body'].read().decode('utf-8')
            return file_content
        except Exception:
            return ''

    def upload(self, bucket_name: str, key: str, file_content: str):
        self.s3_client.upload_fileobj(
            BytesIO(file_content.encode('utf-8')),
            bucket_name,
            key
        )
