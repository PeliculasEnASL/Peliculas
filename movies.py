import streamlit as st
from st_click_detector import click_detector
def images(size):
      content= f"""
         <br>
         <br>
         <a href='#' id='Image 1'><img width='{size}%' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/Frozen2.jpeg'></a>
         <a href='#' id='Image 2'><img width='{size}%' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/TheSantaClause.jpeg'></a>
         <a href='#' id='Image 3'><img width='{size}%' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/puberty.jpg'></a>
         <a href='#' id='Image 4'><img width='{size}%' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/AlmaNochebuena.jpeg'></a>
         <a href='#' id='Image 5'><img width='{size}%' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/christmascarol.jpeg'></a>

         """

      clicked = click_detector(content)
      return clicked
st.title('Peliculas en ASL')
st.header("Español")
clicked = images(50)
# outer_col = st.columns([1,1])
# with outer_col[0]:
#     st.markdown("<a href='https://streamable.com/e/gu49vo?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/Frozen2.jpeg'></a>", unsafe_allow_html=True)
#     st.markdown("<a href='https://streamable.com/e/rpocia?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/TheSantaClause.jpeg'></a>", unsafe_allow_html=True)
#     st.markdown("<a href='https://streamable.com/k0o4gg' target='_blank'><img width='400' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/puberty.jpg'></a>", unsafe_allow_html=True)


# with outer_col[1]:
#     st.markdown("<a href='https://streamable.com/e/xbi2nq?' target='_blank'><img width='400' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/AlmaNochebuena.jpeg'></a>", unsafe_allow_html=True)
#     st.markdown("<a href='https://streamable.com/e/7949vm?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/christmascarol.jpeg'></a>", unsafe_allow_html=True)
 
    


st.header("English")
outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://streamable.com/e/qlc70u?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/Frozen2.jpeg'></a>", unsafe_allow_html=True)

with outer_col[1]:
    st.markdown("<a href='https://streamable.com/e/20rxul?' target='_blank'><img width='200' src='https://raw.githubusercontent.com/PeliculasEnASL/Peliculas/main/images/TheLittleMermaid.jpeg'></a>", unsafe_allow_html=True)


    
