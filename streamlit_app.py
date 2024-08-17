import streamlit as st

st.title('Welcome to Streamlit starter application🎈')

st.info('**Made by: Saim Saqib**')

with st.expander('Accordian'):
  st.write('This is a text which is inside accordian.')

with st.sidebar:
    st.radio("Select your gender:", ['Male', 'Female', 'Custom'])
    st.slider("Select your age:", 18, 45)
    st.selectbox("Select your profession:", ('Data Scientist', 'Blockchain Developer', 'React Developer (Frontend)'))
