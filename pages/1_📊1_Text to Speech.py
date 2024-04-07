import streamlit as st, platform, os
from streamlit import logger
from utils import st_def, ut_vector

st_def.st_logo(title='Text 👋 Speech!', page_title="Text 2 Speech",)
st_def.st_tts()
st.write(platform.processor())
st.write(logger.get_logger("SMI_APP"))
#-----------------------------------------------
from gtts import gTTS
import speech_recognition as sr

def text_to_speech():
    txt_input = st.text_area('Enter the text want to convert to mp3: ', '', height=200)

    with st.form('summarize_form', clear_on_submit=True):
        submitted = st.form_submit_button('Convert Text to Speech')
        
        yn = False
        if submitted:
            st.write('converting ...')
            tts = gTTS(txt_input)
            tts.save("output.mp3")
            os.system("start output.mp3")
            yn = True

    if yn:
        st.write('Finish.')
        with open("output.mp3", "rb") as f:
            data = f.read()
            st.download_button(label="Download File", data=data, file_name="output.mp3", mime="audio/mp3")

        
if __name__ == "__main__":
    text_to_speech()