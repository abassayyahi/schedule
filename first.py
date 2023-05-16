from instagrapi import Client
import streamlit as st

st.title("Post Instagram Photos")

username = st.text_input("Enter your Instagram username")
password = st.text_input("Enter your Instagram password", type="password")
image_path = st.file_uploader("Upload an image for your post", type=["jpg", "jpeg", "png"])
caption = st.text_input("Enter the caption for your post")

if st.button("Post Photo"):
    api = Client()
    api.login(username, password)
    image_file = "uploaded_image.jpg" # choose a name for the permanent file
    with open(image_file, "wb") as f: # open a file with write and binary mode
        f.write(image_path.getvalue()) # write the content of the uploaded file to the permanent file
    api.photo_upload(image_file, caption=caption) # upload the permanent file using its name
    # api.photo_publish(media_id) # publish photo immediately
    st.success("Post published successfully!")