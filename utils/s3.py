import boto3

def download_secrets():
    s3 = boto3.client('s3')
    s3.download_file('siva-s3-bucket-demo', 'secrets/url.json', 'url.json')
    s3.download_file('siva-s3-bucket-demo', 'secrets/service_account.json', 'service_account.json')