import streamlit as st
from PIL import Image

image = Image.open('C:/Users/AuxiliarInstrumentac/Documents/OvationReport/pages/OCR1100.png')

st.image(image, caption='OCR1100.png')
