import streamlit as st

audio_file1 = open('tigre_audio.ogg', 'rb')
audio_bytes1 = audio_file1.read()

audio_file2 = open('elefante_audio.ogg', 'rb')
audio_bytes2 = audio_file2.read()


st.title("animales")

st.image('tigre.jpg')
tigre = st.button('Tigre (Escuchar pronunciación)')
if tigre:
    st.audio(audio_bytes1, format='audio/ogg')
art_tigre = st.text_input('introduce la imagen con su artículo (la primera en mayusculas)')
if art_tigre == 'El tigre':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')


st.image('elefante.jpg')
elefante = st.button('Elefante (Escuchar pronunciación)')
if elefante:
    st.audio(audio_bytes2, format='audio/ogg')
art_elefante = st.text_input('introduce la imagen con su artículo(la primera en mayusculas)')
if art_elefante == 'El elefante':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')