import streamlit as st
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

nltk.download('all')

st.title('Welcome to Streamlit starter application🎈')

st.info('**Made by: Saim Saqib**')

with st.expander('Accordian'):
  st.write('This is a text which is inside accordian.')

with st.sidebar:
    gender = st.radio("Select your gender:", ['Male', 'Female', 'Custom'])
    age = st.slider("Select your age:", 18, 45)
    profession = st.selectbox("Select your profession:", ('Data Scientist', 'Blockchain Developer', 'React Developer (Frontend)'))

st.write('**Gender**:', gender)
st.write('**Age**:', age)
st.write('**Profession**:', profession)
