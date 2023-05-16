import streamlit as st
from instagrapi import Client

# Get user input
username = st.text_input('Enter your Instagram username')
password = st.text_input('Enter your Instagram password', type='password')
image_path = st.text_input('Enter the path to the image you want to upload')
caption = st.text_input('Enter the caption for your post')

# Login to Instagram
cl = Client()
cl.login(username, password)

# Upload photo
if st.button('Schedule Post'):
    cl.photo_upload(image_path, caption)
    st.success('Post scheduled successfully!')