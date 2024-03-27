import os
from dotenv import load_dotenv
from .IDataObject import IDataObject
import boto3
import mimetypes
import magic
import requests


class AwsDataObjectImpl(IDataObject):
    def __init__(self):
        # Load environment variables and set up AWS session and S3 client
        load_dotenv()
        self.session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION"),
        )
        self.s3 = self.session.client("s3")

    def validate_remote_path(self, remote_file_path: str) -> tuple:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        return remote_file_path.split("/", 1)

    def does_exist(self, remote_file_path: str) -> bool:
        try:
            bucket_name, object_name = self.validate_remote_path(remote_file_path)
            self.s3.head_object(Bucket=bucket_name, Key=object_name)
            return True
        except boto3.exceptions.botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return False
            else:
                raise

    def upload(self, file_path: str, remote_file_path: str) -> None:
        bucket_name, object_name = self.validate_remote_path(remote_file_path)
        self.s3.upload_file(file_path, bucket_name, object_name)

    def download(self, remote_file_path: str, local_file_path: str) -> None:
        bucket_name, object_name = self.validate_remote_path(remote_file_path)
        if not self.does_exist(remote_file_path):
            raise ObjectNotFoundException()
        self.s3.download_file(bucket_name, object_name, local_file_path)

    def publish(self, remote_file_path: str, expiration_time: int = 90) -> str:
        bucket_name, object_name = self.validate_remote_path(remote_file_path)
        response = self.s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=expiration_time * 60,
        )
        return response

    def remove(self, remote_file_path: str, recursive: bool = False) -> None:
        bucket_name, object_name = self.validate_remote_path(remote_file_path)
        if recursive:
            bucket = self.session.resource("s3").Bucket(bucket_name)
            bucket.objects.filter(Prefix=object_name).delete()
        else:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)

    def api_call(self, bucket, image_path, remote_full_path):
        file_name_with_extension = self.handle_image_download(image_path)
        if file_name_with_extension:
            remote_full_path = f"{bucket}/{file_name_with_extension}"
        self.upload(image_path, remote_full_path)
        return remote_full_path

    def handle_image_download(self, image_path):
        if image_path.lower().startswith(("http://", "https://")):
            response = requests.get(image_path)
            if response.status_code == 200:
                file_type = magic.from_buffer(response.content, mime=True)
                extension = mimetypes.guess_extension(file_type)
                if not extension:
                    raise ValueError("Could not determine the file extension")
                file_name_with_extension = 'temp_image' + extension
                with open(file_name_with_extension, 'wb') as file:
                    file.write(response.content)
                if os.path.exists(file_name_with_extension):
                    os.remove(file_name_with_extension)
                return file_name_with_extension
            else:
                raise Exception(f"Failed to download image from URL: {image_path}")
        return None

    def is_a_bucket(self):
        # Implementation missing
        pass


class ObjectAlreadyExistsException(Exception):
    def __init__(self, message="The specified object already exists in S3"):
        super().__init__(message)


class ObjectNotFoundException(Exception):
    def __init__(self, message="The specified object was not found in S3"):
        super().__init__(message)


class NotEmptyObjectException(Exception):
    def __init__(self, message="The specified object is not empty"):
        super().__init__(message)
