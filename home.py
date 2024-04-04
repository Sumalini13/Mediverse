import streamlit as st
import json
import requests
from googletrans import Translator
from streamlit_lottie import st_lottie

def app(lk):
    page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/premium-photo/blue-modern-abstract-futuristic-technology-background-23_769134-545.jpg");
background-size: 100%;
background-position: top left;
background-repeat:cover;
background-attachment: local;
}}



[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="column"] {{
background-color: transparent !important;
}}


[data-testid="stToolbar"] {{
right: 2rem;
}}



</style>
"""
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    translator = Translator()
    t="Welcome to MediVerse!"
    tout = translator.translate(t,dest=lk)
    st.title(tout.text)
    w="Explore Us!"
    wout = translator.translate(w,dest=lk)
    st.write(wout.text)

    def load_lf(filepath: str):
        with open(filepath,"r",encoding='utf-8') as f:
            return json.load(f)
    def load_url(url: str):
        r=requests.get(url)
        if r.status_code!=200:
            return None
        return r.json()
    lottie_bot=load_lf(r"C:\Users\Amrut\OneDrive\Desktop\women24\wel.json")
    
    col1, col2 = st.columns([10, 6])
    with col2:
        st.write()
        st.write("\n\n")
        st_lottie(
    lottie_bot,
    speed=2,
    reverse=False,
    loop=True,
    quality="high",
    width="400px",
    height="400px",)


