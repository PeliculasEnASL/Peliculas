import streamlit as st

st.title('Peliculas en ASL')
st.header("Español")

outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://streamable.com/e/gu49vo?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/Frozen2.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://streamable.com/e/rpocia?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/TheSantaClause.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://streamable.com/k0o4gg' target='_blank'><img width='400' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/puberty.jpg'></a>", unsafe_allow_html=True)


with outer_col[1]:
    st.markdown("<a href='https://streamable.com/e/xbi2nq?' target='_blank'><img width='400' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/AlmaNochebuena.jpeg'></a>", unsafe_allow_html=True)
    st.text("Alma's Way Nochebuena")
    st.markdown("<a href='https://streamable.com/e/7949vm?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/christmascarol.jpeg'></a>", unsafe_allow_html=True)
 
    


st.header("English")
outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://streamable.com/e/qlc70u?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/Frozen2.jpeg'></a>", unsafe_allow_html=True)

with outer_col[1]:
    st.markdown("<a href='https://streamable.com/e/20rxul?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/TheLittleMermaid.jpeg'></a>", unsafe_allow_html=True)


    
