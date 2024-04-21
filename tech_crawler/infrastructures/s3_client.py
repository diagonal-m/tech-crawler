from interfaces.storage import Storage

class S3Client(Storage):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def download(self, key: str) -> None:
        print(key)

    def upload(self, key, data):
        print(f"Uploading {key} to S3 bucket {self.bucket_name}")
        # Code to upload file to S3