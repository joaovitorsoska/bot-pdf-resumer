import streamlit as st
from resumidor import resumir_pdf


st.set_page_config(page_title="PDF Resumer")

st.title("PDF resumer com IA")

uploaded_file = st.file_uploader("Envie um PDF", type="pdf")

if uploaded_file is not None:
    st.write("Resumindo o PDF, aguarde um momento...")


    resumo = resumir_pdf(uploaded_file)
    
    st.subheader("Resumo:")
    st.write(resumo)

