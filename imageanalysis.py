import streamlit as st
import pathlib as Path
import google.generativeai as genai
from api_key import api_key
from googletrans import Translator
from languages import *

def app(lk):
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

    system_prompt=""" 
 As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital.Your expertise is curcial in identifyning any anomalies, diseases, or health issues that may be present in the images.
 
 Your Responsibilities include:
 
 1.Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
 2.Findings Report: Document all observed anomalies or signs of disease.Clearly articulate these findings in a structured format.
 3.Recommendation and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
 4.Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

 Important Notes:

 1.Scope of Response: Only respond if the image pertains to human health issues.
 2.Clarity of Image: In cases where image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
 3.Disclaimer:Accompany your analysis with the disclaimer :" Consult with a Doctor before making any decisions."
 4.Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis adhering to the structured approach outlined above.

 Please provide me an output response with these 4 headings in points in each headings and also provide output response according to the Disclaimer in points.
 """

    model = genai.GenerativeModel(model_name="gemini-pro-vision", generation_config=generation_config, safety_settings=safety_settings)

# Set page configuration and theme
#     st.set_page_config(
#     page_title="VitalImage Analytics",
#     page_icon=":robot",
   
# )

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


#title
    translator = Translator()
    o = translator.translate("Vital Image Analytics 👩‍⚕️🩺",dest=lk)
    p = translator.translate("An application designed to assist in the identification of medical images",dest=lk)
    u= translator.translate("Upload the medical image for analysis",dest=lk)
    c= translator.translate("Uploaded Image",dest=lk)
    s= translator.translate("Select target language:",dest=lk)
    b= translator.translate("Generate the Analysis",dest=lk)
    tt= translator.translate("Here is the analysis based on your image: ",dest=lk)
    
    st.title(o.text)
    st.subheader(p.text)
    uploaded_file=st.file_uploader(u.text, type=["png","jpg","jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption=c.text)
    target_language = st.selectbox(s.text, languages,index=languages.index(lk))
       
    submit_button=st.button(b.text)
    if submit_button:
        image_data=uploaded_file.getvalue()
        image_parts=[
        {
            "mime_type":"image/jpeg",
            "data":image_data
        },
    ]

        prompt_parts=[
        image_parts[0],
        system_prompt,
    ]
    
        response=model.generate_content(prompt_parts)
        if response:
            translator = Translator()
            st.title(tt.text)
            out = translator.translate(response.text,dest=target_language)
            st.write(out.text)





