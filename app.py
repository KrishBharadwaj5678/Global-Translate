import streamlit as st
from googletrans import LANGUAGES
from deep_translator import GoogleTranslator


# Defining Page Title,Icon
st.set_page_config(
    page_title="Global Translate",
    page_icon="global.png",
    menu_items={
        "About":"Global Translate brings the world to your fingertips with its powerful translation engine. Effortlessly communicate across borders and cultures with precision and ease."
    }
)

# Get the dictionary of supported languages
lang=[f"{code} : {name}" for code, name in LANGUAGES.items()]

st.write("<h3 style='color:#FF8A08;'>Break Language Barriers with Our Powerful Translation Tool!</h3>",unsafe_allow_html=True)

text=st.text_input("Enter Your Text")

selected_lang_input=st.selectbox("Specify the language for the above text",lang,index=lang.index("en : english"))

selected_lang_output=st.selectbox("Select language for translation",lang,index=lang.index("en : english"))

btn=st.button("Generate")

if btn:
    try:
        translation = GoogleTranslator(source=selected_lang_input.split(":")[0].strip(), target=selected_lang_output.split(":")[0].strip()).translate(text)
        st.markdown("### :green[Translated Text:]")
        st.code(translation)
    except:
        st.error("Please Enter Something...")
