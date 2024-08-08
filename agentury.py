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
    # st.write(df_agentury)

    df_agentury_rollup_loc = df_agentury[df_agentury['Agentura'] == 'Rollup']

    df_agentury_start_loc = df_agentury[df_agentury['Agentura'] != '']

    df_agentury_end_loc = df_agentury[df_agentury['Klient'] == 'Rollup']

    names_list = df_agentury_start_loc["Agentura"].to_list()
    names = list(dict.fromkeys(names_list))
    del names[-1]

    del names_list[-1]

    def my_index_multi(l, x):
        return [i for i, _x in enumerate(l) if _x == x]

    start_list = []

    for i in range(len(names)):
        name = names[i]
        idx_list = my_index_multi(names_list, name)
        start_list.append(idx_list[0]+1)

    end_list = []
    for row in df_agentury_end_loc.index:
        end_list.append(row+1)

    source_file = 'rev.xlsx'
    item_num = len(start_list)

    # zip_file = zipfile.ZipFile('splitted_agentury.zip', 'w')

    for i in range(len(start_list)):
        start_num = start_list[i]
        end_num = end_list[i]+1
        name = names[i]
        name = re.sub('s\.\s?r\.\s?o\.\s?', 'sro', name)
        name = re.sub('a\.\s?s\.\s?', 'as', name)
        name = re.sub('\.|,', '', name)
        name = re.sub('\s', '_', name).lower()
    #     print(name)
        book = openpyxl.load_workbook(source_file)
        sheet = book['1. Revenue agentury pilot RU...']
        sheet.delete_rows(1, 4)
        
        if i == 0:
    #         print(f"First: {name}, End num: {end_num+1}")
            sheet.delete_rows(end_num+1, 10000)
        elif i+1 == item_num:
            sheet.delete_rows(end_num+1, end_num+1)
            sheet.delete_rows(2, start_num-1)
        else:
            # není první ani poslední
            sheet.delete_rows(end_num+1, 10000)
            sheet.delete_rows(2, start_num-1)
            
        sheet.delete_cols(1, 1)
        sheet.delete_cols(2, 1)

        output_file = f'{name}.xlsx'

        book.save(output_file)


        
        
    # zip_file.close()

