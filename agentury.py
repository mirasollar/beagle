import streamlit as st
import pandas as pd
import openpyxl
import re
# import zipfile
# from tempfile import NamedTemporaryFile

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None and uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
    df_raw = pd.read_excel('rev.xlsx', nrows=20)
    header_loc = df_raw[df_raw == 'Agentura'].dropna(axis=1, how='all').dropna(how='all')
    header_row = header_loc.index.item()
    df_agentury = pd.read_excel('rev.xlsx', header=header_row+1)
    st.write(df_agentury)
