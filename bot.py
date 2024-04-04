import streamlit as st
import pathlib as Path
import google.generativeai as genai
from api_key import api_key
import speech_recognition
from googletrans import Translator
from languages import *
from language_codes import languages_codes
import pyttsx3
from gtts import gTTS
from voice_codes import codes

import json
import requests
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


[data-testid="stToolbar"] {{
right: 2rem;
}}



</style>
"""
    st.markdown(page_bg_img, unsafe_allow_html=True)



    def load_lf(filepath: str):
        with open(filepath,"r",encoding='utf-8') as f:
            return json.load(f)
    def load_url(url: str):
        r=requests.get(url)
        if r.status_code!=200:
            return None
        return r.json()
    lottie_bot=load_lf(r"C:\Users\Amrut\OneDrive\Desktop\women24\chatbot.json")
    col1, col2 = st.columns([10, 4])
    with col1:
        genai.configure(api_key=api_key)
        generation_config = {  "temperature": 0.4,  "top_p": 1,  "top_k": 32,
"max_output_tokens": 4096,
}
        safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE" },
{"category": "HARM_CATEGORY_HATE_SPEECH",  "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",  "threshold": "BLOCK_MEDIUM_AND_ABOVE"  }, 
{   "category": "HARM_CATEGORY_DANGEROUS_CONTENT",   "threshold": "BLOCK_MEDIUM_AND_ABOVE" },
]
        prompt="""You are a medical chatbot designed to assist users with health-related inquiries . 
You will analyze the given text, which may contain patient symptoms, medical history, or queries,
and provide relevant information, advice, or guidance based on your medical knowledge and expertise. 
Please review the text and offer appropriate responses, suggestions, or explanations tailored to the user's needs."""
        def generate_gemini_content(textt,prompt,target_language):
            model=genai.GenerativeModel("gemini-pro")
            response=model.generate_content(prompt+textt)
            translator = Translator()
            out = translator.translate(response.text,dest=target_language)
            return out
            

        translator = Translator()
        w = translator.translate("Start speaking...",dest=lk)
        def recognize_speechhh(languages):
            sr = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                sr.adjust_for_ambient_noise(source, duration=2)
                st.write(w.text)
                audio = sr.listen(source)
                lan=str(languages)
                l=languages_codes.get(lan)
                lang=str(l)
                text = sr.recognize_google(audio,language=lang)
                text = text.lower()
            return text  
          
        t = translator.translate("MediBot ",dest=lk)
        i = translator.translate("Enter Your Queries:",dest=lk)
        d = translator.translate("Select target language:",dest=lk)
        dd = translator.translate("Did you say: ",dest=lk)
        tr = translator.translate("Text Response",dest=lk)
        ar = translator.translate("Audio Response",dest=lk)
 
        st.title(t.text)
        input=st.text_input(i.text)
        target_language = st.selectbox(d.text, languages,index=languages.index(lk))
        if st.button("🎙"):
            text = recognize_speechhh(target_language)
            st.write(dd.text, text)
            translator = Translator()
            out = translator.translate(text,dest="English")
            res=generate_gemini_content(out.text,prompt,target_language)
            st.write(res.text)
            
        if st.button(tr.text):
            if input:
                translator = Translator()
                out = translator.translate(input,dest="English")
                res=generate_gemini_content(out.text,prompt,target_language)
                st.write(res.text)
                
        if st.button(ar.text):
            if input:
                translator = Translator()
                out = translator.translate(input,dest="English")
                res=generate_gemini_content(out.text,prompt,target_language)
                lan=str(target_language)
                l=codes.get(lan)
                la=str(l)
                k=res.text
                b=k.replace("**", "")
                bb=b.replace("*", "")
                output = gTTS(text=bb, lang = la, slow = False)
                output.save("output.mp3")
                st.audio("output.mp3", format='audio/mp3')

           
                
                

        


    with col2:
        st_lottie(
    lottie_bot,
    speed=2,
    reverse=False,
    loop=True,
    quality="high",
    width="250px",
    height="200px"
)