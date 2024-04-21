import streamlit as st

audio_file1 = open('azul_audio.ogg', 'rb')
audio_bytes1 = audio_file1.read()

audio_file2 = open('blanco_audio.ogg', 'rb')
audio_bytes2 = audio_file2.read()

st.title("colores")

st.image('azul.jpg')
azul = st.button('Azul (Escuchar pronunciación)')
if azul:
    st.audio(audio_bytes1, format='audio/ogg')
art_azul = st.text_input('introduce la imagen con su artículo (la primera en mayusculas)')
if art_azul == 'El azul':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')


st.image('blanco.jpg')
blanco = st.button('blanco (Escuchar pronunciación)')
if blanco:
    st.audio(audio_bytes2, format='audio/ogg')
art_blanco = st.text_input('introduce la imagen con su artículo(la primera en mayusculas)')
if art_blanco == 'El blanco':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')