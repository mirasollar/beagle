import streamlit as st
import pandas as pd
import openpyxl
import re
# import zipfile
# from tempfile import NamedTemporaryFile
from io import StringIO
import os
from pathlib import Path

def saveFile(uploaded):
    with open(os.path.join(os.getcwd(),uploaded.name),"w") as f:
        strIo= StringIO(uploaded.getvalue().decode("utf-8"))
        f.write(strIo.read())
        return os.path.join(os.getcwd(),uploaded.name)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    fpath=saveFile(uploaded_file)
    st.write(f"Cesta je: {fpath}")
    st.write(f"Soubor je: {uploaded_file}")

    st.write(f"Directory je: {os.listdir()}")
