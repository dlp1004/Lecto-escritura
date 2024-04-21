import streamlit as st

audio_file1 = open('manzana_audio.ogg', 'rb')
audio_bytes1 = audio_file1.read()

audio_file2 = open('sandia_audio.ogg', 'rb')
audio_bytes2 = audio_file2.read()


st.title("Fruta")

st.image('manzana.jpg')
manzana = st.button('Manzana (Escuchar pronunciación)')
if manzana:
    st.audio(audio_bytes1, format='audio/ogg')
art_manzana = st.text_input('introduce la imagen con su artículo (la primera en mayusculas)')
if art_manzana == 'La manzana':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')


st.image('sandia.jpg')
sandia = st.button('Sandia (Escuchar pronunciación)')
if sandia:
    st.audio(audio_bytes2, format='audio/ogg')
art_sandia = st.text_input('introduce la imagen con su artículo(la primera en mayusculas)')
if art_sandia == 'La sandia':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce la oración correcta!')