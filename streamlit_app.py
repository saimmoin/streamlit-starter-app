import streamlit as st
import PyPDF2
import google.generativeai as genai

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barriecito&family=Dancing+Script&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Barriecito', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Welcome to Interprep AI🎈')

st.info('**Interprep: Your Gateway to Real-World Job Success – Empowering Fresh Graduates to Ace Their Career Journey.**')

with st.expander('Accordian'):
  st.write('This is a text which is inside accordian.')

with st.sidebar:
    gender = st.radio("Select your gender:", ['Male', 'Female', 'Custom'])
    age = st.slider("Select your age:", 18, 45)
    profession = st.selectbox("Select your profession:", ('Data Scientist', 'Blockchain Developer', 'React Developer (Frontend)'))

st.write('**Gender**:', gender)
st.write('**Age**:', age)
st.write('**Profession**:', profession)
