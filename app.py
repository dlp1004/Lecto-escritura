import streamlit as st

# Fetch the service account key JSON file contents

# Initialize the app with a service account, granting admin privileges

st.set_page_config(
    page_title="Lecto-escritura UBU",
    page_icon="📖",
)

st.title("Lecto-escritura")
st.sidebar.success("Select a page above.")

st.text('¡Bienvenido a nuestra aplicación de lecto-escritura! \nSelecciona una categoría en la lista de la izquierda para empezar a jugar ')