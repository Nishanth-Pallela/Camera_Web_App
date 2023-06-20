import streamlit as st
from PIL import Image
uploaded_image = st.file_uploader('Upload Image')
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)


with st.expander('Start Camera'):
    # Start Camera
    picture = st.camera_input('Camera')
    print(picture)

    if picture:
        # Create a pillow image instance

        img = Image.open(picture)
        gray_img = img.convert("L")
        # Render the gray scale image
        st.image(gray_img)
