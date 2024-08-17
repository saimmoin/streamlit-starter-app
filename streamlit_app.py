import streamlit as st

st.title('Welcome to Streamlit starter application🎈')

st.info('**Made by: Saim Saqib**')

with st.expander('Accordian'):
  st.write('This is a text which is inside accordian.')

with st.sidebar:
    st.radio("Select one:", [1, 2])
