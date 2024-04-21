import streamlit as st

if 'text' not in st.session_state:
	st.session_state.text = ''

st.title("Scramble")

st.image('nino_sed.jpg')

sed = st.button('sed')
if sed:
    st.session_state.text = st.session_state.text + 'sed '

niño = st.button('niño')
if niño:
    st.session_state.text = st.session_state.text + 'niño '

el = st.button('El')
if el:
    st.session_state.text = st.session_state.text + 'El '

tiene = st.button('tiene')
if tiene:
    st.session_state.text = st.session_state.text + 'tiene '

reset = st.button('Borrar texto')
if reset:
    st.session_state.text = ''



st.text(st.session_state.text)

if st.session_state.text == 'El niño tiene sed ':
    st.text('¡Muy bien!')
else:
    st.text('¡Introduce el texto correcto!')