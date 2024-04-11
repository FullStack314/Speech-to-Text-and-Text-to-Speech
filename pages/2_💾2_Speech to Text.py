# import sys, os
# if "STREAMLIT_SERVER_ENABLED" in os.environ and "IS_STREAMLIT_SERVER" in os.environ: __import__('pysqlite3'); sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from utils import st_def

import chromadb     #0.4.24
from   chromadb.utils import embedding_functions

st_def.st_logo(title='Speech to Text 👋!', page_title="Welcome ASR! ",)
st_def.st_asr()
#-----------------------------------------------
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Speak...")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    speech_to_text()