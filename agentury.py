import os
import pandas as pd

def saveFile(uploaded):
    # Určete cestu, kam se soubor uloží
    file_path = os.path.join(os.getcwd(), uploaded.name)
    
    # Získání obsahu souboru jako bytes
    content = uploaded.getvalue()
    
    # Načtení obsahu do pandas DataFrame
    excel_data = pd.read_excel(BytesIO(content), engine='openpyxl')
    
    # Uložení souboru na disk
    with open(file_path, "wb") as f:
        f.write(content)
    
    return file_path, excel_data


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    fpath=saveFile(uploaded_file)
    st.write(f"Cesta je: {fpath}")
    st.write(f"Soubor je: {uploaded_file}")

    st.write(f"Directory je: {os.listdir()}")
