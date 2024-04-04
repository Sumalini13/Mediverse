import streamlit as st
from streamlit_option_menu import option_menu
import imageanalysis,bot,home,health
from googletrans import Translator
from languages import *

page_bg_img = f"""
<style>
[data-testid="stSidebar"] {{
background-image: url("https://i.pinimg.com/564x/a1/78/77/a178771c7cefe3417ac6b440b97640d5.jpg");
background-size: 100%;
background-position: top left;
background-repeat:cover;
background-attachment: local;
}}
</style>
"""
st.set_page_config(
    page_title="MediVerse",
    page_icon="🧊",
    layout="wide", initial_sidebar_state="auto",
)
st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.header('Language')
language = st.sidebar.selectbox('Select Language', languages, index=0)
h="Home"
m="MediBot"
mv="MediVision"
mp="Prescription"
translator = Translator()
hout = translator.translate(h,dest=language)
mout = translator.translate(m,dest=language)
mvout = translator.translate(mv,dest=language)
mp_out = translator.translate(mp,dest=language)


sel = option_menu(None, [hout.text, mout.text, mvout.text , mp_out.text], 
        icons=['house','robot','image','image-fill'], menu_icon="cast", default_index=0,
        orientation="horizontal",
styles={
        "container": {"padding": "0!important", "background-color": "black"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "px", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "darkblue"},
    }
)

    
if(sel==hout.text):
    home.app(language)
if(sel==mvout.text):
    imageanalysis.app(language)
if(sel==mout.text):
    bot.app(language)
if(sel==mp_out.text):
    health.app(language)
 

