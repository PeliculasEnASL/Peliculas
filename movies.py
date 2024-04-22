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
         # <a href='#' id='Image 6'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/f.gif'></a>
         # <a href='#' id='Image 7'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/g.gif'></a>
         # <a href='#' id='Image 8'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/h.gif'></a>
         # <a href='#' id='Image 9'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/i.gif'></a>
         # <a href='#' id='Image 10'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/j.gif'></a>
         # <a href='#' id='Image 11'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/k.gif'></a>
         # <a href='#' id='Image 12'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/l.gif'></a>
         # <a href='#' id='Image 13'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/m.gif'></a>
         # <a href='#' id='Image 14'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/n.gif'></a>
         # <a href='#' id='Image 15'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/o.gif'></a>
         # <a href='#' id='Image 16'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/p.gif'></a>
         # <a href='#' id='Image 17'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/q.gif'></a>
         # <a href='#' id='Image 18'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/r.gif'></a>
         # <a href='#' id='Image 19'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/s.gif'></a>
         # <a href='#' id='Image 20'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/t.gif'></a>
         # <a href='#' id='Image 21'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/u.gif'></a>
         # <a href='#' id='Image 22'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/v.gif'></a>
         # <a href='#' id='Image 23'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/w.gif'></a>
         # <a href='#' id='Image 24'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/x.gif'></a>
         # <a href='#' id='Image 25'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/y.gif'></a>
         # <a href='#' id='Image 26'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/z.gif'></a>
         # <a href='#' id='Image 27'><img width='{size}%' src='https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_1414/BabySignLanguage/DictionaryPages/another-webp.webp'></a>
         """

      clicked = click_detector(content)
      return clicked
st.title('Peliculas en ASL')
st.header("Español")
clicked = images(2)
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


    
