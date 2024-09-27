import streamlit as st
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import pycountry

# To ensure consistent results for the same input
DetectorFactory.seed = 0

# Function to convert language code to full name
def get_language_name(language_code):
    try:
        return pycountry.languages.get(alpha_2=language_code).name
    except AttributeError:
        return "Unknown"

# Streamlit UI
st.title('Automatic Language Detection')

# Input text from user
user_input = st.text_area("Enter the text you want to detect the language of:")

# Perform language detection when the user enters some text
if st.button('Detect Language'):
    if user_input:
        try:
            # Detect the language
            language_code = detect(user_input)
            language_name = get_language_name(language_code)
            st.success(f'The detected language is: {language_name}')
        except LangDetectException:
            st.error('Could not detect the language. Please enter a valid text.')
    else:
        st.warning("Please enter some text for detection.")
