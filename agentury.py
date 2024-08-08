import streamlit as st
import pandas as pd
import openpyxl
import re
# import zipfile
# from tempfile import NamedTemporaryFile
import os


uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    st.write(f"Soubor je: {uploaded_file}")

    st.write(f"Directory je: {os.listdir()}")
