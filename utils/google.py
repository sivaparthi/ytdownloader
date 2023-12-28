from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

f = open('url.json')
data = json.load(f)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = data['url_id']

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_photo(file_path, filename):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : filename,
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

    return file

def get_sharable_link(file_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    request_body = {
        'role' : 'reader',
        'type' : 'anyone'
    }

    response_permission = service.permissions().create(
        fileId = file_id,
        body = request_body
    ).execute()

    response_share_link = service.files().get(
        fileId=file_id,
        fields='webViewLink'
    ).execute()

    return response_permission, response_share_link
