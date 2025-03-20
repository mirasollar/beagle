import os
import tempfile
import streamlit as st
from PIL import Image, ImageFilter
import requests
import random
from streamlit_js_eval import streamlit_js_eval
import base64
from io import BytesIO
import json
import pandas as pd

def blurred_centered_image(img_url, blur_num):
    response = requests.get(img_url, stream=True)
    img = Image.open(response.raw).filter(ImageFilter.GaussianBlur(blur_num))
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    style_str = f"""
        <style>
        .centered-image {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;
            margin-bottom: 20px;
        }}
        </style>
        <img src="data:image/jpeg;base64,{img_str}" class="centered-image">
        """
    return style_str

if "tmp_file_path" not in st.session_state:
    tmp_dir = tempfile.gettempdir()  # Získá systémový temp adresář
    st.session_state.tmp_file_path = os.path.join(tmp_dir, "dogs_data.json")

TMP_FILE_PATH = st.session_state.tmp_file_path

def init_file():
    if not os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "w") as f:
            json.dump({"dogs": []}, f)  # Uložíme prázdný JSON objekt

def write_to_file(dog_name, result):
    data = read_file()  # Načteme aktuální obsah
    data["dogs"].append([dog_name, result])  # Přidáme nové jméno do pole
    with open(TMP_FILE_PATH, "w") as f:
        json.dump(data, f)  # Přepíšeme soubor s novým seznamem

def read_file():
    if os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r") as f:
            return json.load(f)
    return {"dogs": []}

data = read_file()

excluded_dogs = {sublist[0] for sublist in data["dogs"]} if data["dogs"] else set()

all_dogs = [["bichon_frise.jpg", "Bichon Frise"], ["irish_setter.jpg", "Irish Setter"], ["german_shepherd.jpg", "German Shepherd"]]

# all_dogs = [["german_shepherd.jpg", "German Shepherd"], ["labrador_retriever.jpg", "Labrador Retriever"], ["english_bulldog.jpg", "English Bulldog"],
#             ["lhasa_apso.jpg", "Lhasa Apso"], ["jack_russel_terrier.jpg", "Jack Russell Terrier"], ["border_collie.jpg", "Border Collie"]]
filtered_dogs = [dog for dog in all_dogs if dog[1] not in excluded_dogs]

if filtered_dogs:
    # st.write("Aktuální obsah souboru:")
    # st.text(read_file())
    # st.write(f"Excluded dogs: {excluded_dogs}")
    # st.write(f"Filtered dogs: {filtered_dogs}")

    if 'image_url' not in st.session_state and 'dog_name' not in st.session_state:
        # random.shuffle(all_dogs)
        st.session_state.image_url = f"https://miroslavsollar.cz/dogs/{filtered_dogs[0][0]}"
        st.session_state.dog_name = filtered_dogs[0][1]

    if 'number' not in st.session_state:
        st.session_state.number = 50

    def subtract():
        if st.session_state.number > 0:
            st.session_state.number -= 6

    if 'count' not in st.session_state:
        st.session_state.count = 0

    def increment_counter():
        st.session_state.count += 1

    if "win" not in st.session_state:
        st.session_state.win = False

    if st.session_state.win == False:
        st.title(f"Number of remaining attempts: {6-st.session_state.count}")

    st.markdown(blurred_centered_image(st.session_state.image_url, st.session_state.number), unsafe_allow_html=True) 

    if "show_focus_button" not in st.session_state:
        st.session_state.show_focus_button = True

    def toggle_button():
        st.session_state.show_focus_button = not st.session_state.show_focus_button

    if st.session_state.show_focus_button:
        if st.session_state.count < 6:
            if st.button("Reduce blur", on_click=increment_counter, type="primary", use_container_width=True):
                subtract()
                st.rerun()
        else:
            toggle_button()
        option = st.selectbox(
            "Choose a breed.",
            ("Afghan Hound", "Akita", "Alaskan Malamute", "American Bulldog", "American Cocker Spaniel", 
    "American Foxhound", "American Pit Bull Terrier", "Australian Cattle Dog", "Australian Shepherd", 
    "Australian Terrier", "Airedale Terrier", "Bernese Mountain Dog", "Basset Hound", "Beagle", 
    "Belgian Malinois", "Bichon Frise", "Bloodhound", "Border Collie", "Borzo", "Boxer", "Bulldog", 
    "Bull Terrier", "Cairn Terrier", "Cavalier King Charles Spaniel", "Chesapeake Bay Retriever", 
    "Chihuahua", "Chinese Shar-Pei", "Cockapoo", "Collie", "Cocker Spaniel", "Curly-Coated Retriever", 
    "Dachshund", "Doberman Pinscher", "English Bulldog", "English Foxhound", "English Setter", 
    "English Springer Spaniel", "French Bulldog", "German Shepherd", "German Shorthaired Pointer", 
    "Glen of Imaal Terrier", "Golden Doodle", "Golden Retriever", "Great Dane", "Havanese", 
    "Irish Setter", "Irish Water Spaniel", "Italian Greyhound", "Jack Russell Terrier", "Labrador Retriever", 
    "Labradoodle", "Lhasa Apso", "Maltese", "Manchester Terrier", "Miniature Pinscher", 
    "Miniature Schnauzer", "Moscow Watchdog", "Newfoundland", "Norfolk Terrier", "Norwegian Elkhound", 
    "Papillon", "Pit Bull Terrier", "Pointer", "Pomeranian", "Poodle", "Pug", "Rat Terrier", "Rottweiler", 
    "Russian Wolfhound", "Saint Bernard", "Samoyed", "Scotch Terrier", "Shiba Inu", "Shih Tzu", "Silky Terrier", 
    "Shetland Sheepdog", "Soft Coated Wheaten Terrier", "Whippet", "Yorkshire Terrier"),
            index=None,
            placeholder="Choose the breed of dog...",
        )

    if st.session_state.show_focus_button == False:
        
        if st.session_state.win == False:
            st.title(f"You lost! Correct answer: {st.session_state.dog_name}")
        st.markdown(blurred_centered_image(st.session_state.image_url, 0), unsafe_allow_html=True)
        if len(filtered_dogs) > 1:
            if st.button("Continue", type="primary", use_container_width=True):
                toggle_button()
                if st.session_state.win == False: 
                    write_to_file(st.session_state.dog_name, "Lost")
                else:
                    write_to_file(st.session_state.dog_name, "Win")
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
        else:
            if st.button("Go to Results Page", type="primary", use_container_width=True):
                if st.session_state.win == False: 
                    write_to_file(st.session_state.dog_name, "Lost")
                else:
                    write_to_file(st.session_state.dog_name, "Win")
                streamlit_js_eval(js_expressions="parent.window.location.reload()")


    if st.session_state.show_focus_button == True:
        if st.button("Confirm", type="primary", use_container_width=True):
            if st.session_state.count > 5:
                toggle_button() 
            else:
                if option == st.session_state.dog_name:
                    st.markdown(blurred_centered_image(st.session_state.image_url, 0), unsafe_allow_html=True)
                    toggle_button()
                    st.session_state.win = True
                elif option is None:
                    pass
                elif option != st.session_state.dog_name:
                    increment_counter()
            st.rerun()

    if st.session_state.win:
        st.title("You won!")
        st.write(f"{st.session_state.dog_name}. Number of attempts: {st.session_state.count}")

else:
    st.title("Results")
    df = pd.DataFrame(data['dogs'], columns=['Breed', 'Result'])
    st.dataframe(df, hide_index=True)

    if st.button("New Game"):
        os.remove(TMP_FILE_PATH)
        init_file()
        st.rerun()
