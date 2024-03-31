import streamlit as st

st.title('Peliculas en ASL')
st.header("Español")
outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://streamable.com/e/gu49vo?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/download.jpeg'></a>", unsafe_allow_html=True)

st.header("English")
outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://streamable.com/e/qlc70u?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/download.jpeg'></a>", unsafe_allow_html=True)

    