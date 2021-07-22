import constants
import boto3


class StorageService:
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )

    def upload_file(self, path: str, name: str):
        self.s3.upload_file(path, constants.YANDEX_BUCKET_NAME, name)

    def delete_file(self, name: str):
        for_deletion = [{'Key': name}]
        self.s3.delete_objects(Bucket=constants.YANDEX_BUCKET_NAME, Delete={'Objects': for_deletion})

    def get_objects(self):
        objects = self.s3.list_objects(Bucket=constants.YANDEX_BUCKET_NAME).get('Contents')
        if objects:
            print('Objects:')
            for key in self.s3.list_objects(Bucket=constants.YANDEX_BUCKET_NAME)['Contents']:
                print(key['Key'])
        else:
             print('No objects')