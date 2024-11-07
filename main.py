import streamlit as st
import PyPDF2

# Titre de l'application
st.title("PDF to MP3")

# Création du bouton "Load"
if st.button("Upload"):
    # Sélection et chargement du fichier
    uploaded_file = st.file_uploader("Select a file", type="pdf")

    # Vérifier si un fichier a été chargé
    if uploaded_file is not None:
        st.success("File loaded!")

        # Afficher le nom du fichier
        st.write("File name:", uploaded_file.name)


    else:
        st.warning("No file selected.")
