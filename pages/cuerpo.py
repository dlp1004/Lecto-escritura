import streamlit as st

audio_file1 = open('cabeza_audio.ogg', 'rb')
audio_bytes1 = audio_file1.read()

audio_file2 = open('pierna_audio.ogg', 'rb')
audio_bytes2 = audio_file2.read()

st.title("partes del cuerpo")

st.image('cabeza.jpg')
cabeza = st.button('Cabeza (Escuchar pronunciación)')
if cabeza:
    st.audio(audio_bytes1, format='audio/ogg')
art_cabeza = st.text_input('introduce la imagen con su artículo (la primera en mayusculas)')
if art_cabeza == 'La cabeza':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')


st.image('pierna.jpg')
pierna = st.button('Pierna (Escuchar pronunciación)')
if pierna:
    st.audio(audio_bytes2, format='audio/ogg')
art_pierna = st.text_input('introduce la imagen con su artículo(la primera en mayusculas)')
if art_pierna == 'La pierna':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')