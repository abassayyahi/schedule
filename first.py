import streamlit as st
from instagrapi import Client
from PIL import Image
import tempfile

# Get user input
username = st.text_input('Enter your Instagram username')
password = st.text_input('Enter your Instagram password', type='password')
caption = st.text_input('Enter the caption for your post')

# Login to Instagram
cl = Client()

if st.button('Login'):
    cl.login(username, password)
    st.success('Logged in successfully!')

# Upload photo
uploaded_file = st.file_uploader('Choose an image to upload', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Create a temporary file to save the uploaded image
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        fp.write(uploaded_file.getvalue())
        image_path = fp.name

    if st.button('Schedule Post'):
        cl.photo_upload(image_path, caption)
        st.success('Post scheduled successfully!')