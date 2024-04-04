### Health Management APP

import streamlit as st
import google.generativeai as genai
from PIL import Image
from googletrans import Translator
from languages import *

from api_key import api_key

def app(lk):
    genai.configure(api_key=api_key)
    def get_gemini_repsonse(input,image):
        model=genai.GenerativeModel('gemini-pro-vision')
        response=model.generate_content([input,image[0]])
        return response.text
    
    page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/premium-photo/blue-modern-abstract-futuristic-technology-background-23_769134-545.jpg");
background-size: 100%;
background-position: top left;
background-repeat:cover;
background-attachment: local;
}}


[data-testid="stToolbar"] {{
right: 2rem;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

</style>
"""
    st.markdown(page_bg_img, unsafe_allow_html=True)


    def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
        # Read the file into bytes

            image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

    translator = Translator()
    t= translator.translate("Medical Prescription Extractor",dest=lk)
    sh= translator.translate("Streamlining Medicine Name Extraction from Medical Prescriptions",dest=lk)
    uf=translator.translate("Choose an image...",dest=lk)
    ss=translator.translate("Select target language:",dest=lk)
    up=translator.translate("Uploaded Image!",dest=lk)
    b=translator.translate("Generate Response",dest=lk)
    rt=translator.translate("The Response is",dest=lk)
    st.title(t.text)
    st.subheader(sh.text)
    uploaded_file = st.file_uploader(uf.text, type=["jpg", "jpeg", "png"])
    image=""   
    target_language = st.selectbox(ss.text, languages,index=languages.index(lk))
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption=up.text, use_column_width=True)


    submit=st.button(b.text)

    input_prompt="""
Extract the names from the following medical prescription:

Prescription:
Patient Name: [Patient's Name]
Age: [Patient's Age]
Date: [Date of Prescription]

Medications:
1. [Medicine 1]
2. [Medicine 2]
3. [Medicine 3]
4. [Medicine 4]
...

Instructions:

Identify and extract the names of medicines listed in the prescription.
List all the medicines mentioned, one per line.

"""

## If submit button is clicked

    if submit:
        image_data=input_image_setup(uploaded_file)
        response=get_gemini_repsonse(input_prompt,image_data)
        st.subheader(rt.text)
        translator = Translator()
        out = translator.translate(response,dest=target_language)
        st.write(out.text)
    

