import streamlit as st

audio_file = open('Casa_audio_prueba.mp4', 'rb')
audio_bytes = audio_file.read()


st.title("Casa")

st.image('casa.jpg')
casa = st.button('Casa (Escuchar pronunciación)')
if casa:
    st.audio(audio_bytes, format='audio/mp4')
art_casa = st.text_input('introduce la imagen con su artículo (la primera en mayusculas)')
if art_casa == 'La casa':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')