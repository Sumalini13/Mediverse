import speech_recognition
import pyttsx3
import streamlit as st

# Function to recognize speech
def recognize_speechhh():
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        st.write("Silence please...")
        sr.adjust_for_ambient_noise(source, duration=2)
        st.write("Speak now please...")
        audio = sr.listen(source)
        text = sr.recognize_google(audio)
        text = text.lower()
    return text

# Main Streamlit app
def main():
    st.title("Speech Recognition App")
    st.write("Press the button and speak")

    if st.button("🎙"):
        text = recognize_speechhh()
        st.write("Did you say: ", text)

if __name__ == "__main__":
    main()
