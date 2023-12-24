import streamlit as st
from utils.downloader import download_video
from utils.delete_vids import delete_all_files_in_folder

st.title("YT video Downloader")
delete_all_files_in_folder('vids')

url = st.text_input('video link')
if url:
    output, filename = download_video(url)
    st.write("video received")
    st.video('vids/'+filename+'.mp4')

