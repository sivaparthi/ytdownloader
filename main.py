import streamlit as st
from utils.downloader import download_video
from utils.delete_vids import delete_all_files_in_folder
from utils.s3 import download_secrets

download_secrets()
from utils.google import upload_photo, get_sharable_link

st.title("YT video Downloader")
delete_all_files_in_folder('vids')

url = st.text_input('video link')
if url:
    output, filename = download_video(url)
    file = upload_photo("vids/"+filename+'.mp4', filename=filename)
    file_id = file['id']
    permission, link = get_sharable_link(file_id=file_id)
    st.write(link['webViewLink'])
    st.success('Done')