import streamlit as st
# import PyPDF2
import time

from streamlit_pdf_viewer import pdf_viewer
from streamlit import session_state as ss
from pypdf import PdfReader


# App title
st.title("PDF to Podcast")

# Declare variable that will keep the pdf file
if 'pdf_ref' not in ss:
    ss.pdf_ref = None

# Select file to load
uploaded_file = st.file_uploader("Select a .pdf file", type="pdf", key='pdf')
if ss.pdf:
    ss.pdf_ref = ss.pdf

# Check if file loading is OK
if uploaded_file is not None:
    message = st.success("File loaded !")

    if st.button("Start conversion"):
        message.empty()

        with st.spinner('Converting...'):

            # Fake calcul time
            time.sleep(2)

            reader = PdfReader(uploaded_file)
            numberOf_pages = len(reader.pages)
            progress_bar = st.progress(0)       # Progression bar

            extracted_text = ""
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                extracted_text += text + "\n"

                # Update progress bar
                progress = (i + 1) / numberOf_pages
                progress_bar.progress(progress)
                time.sleep(0.1)     # Fake calcul time between each page

            st.write(extracted_text)

    # Display file
    if ss.pdf_ref:
        binary_data = ss.pdf_ref.getvalue()
        pdf_viewer(input=binary_data, width=700)

else:
    st.warning("No file selected.")
