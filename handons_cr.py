import streamlit as st
from PIL import Image   
st.title("My first ML app")

st.markdown("# Main page")
st.sidebar.markdown("## Main Page")
image = Image.open('sunrise.jpg')
st.image(image, caption='ueueueue')


