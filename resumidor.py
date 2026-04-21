from dotenv import load_dotenv
import os
from groq import Groq
from PyPDF2 import PdfReader

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)


def resumir_pdf(file):
    leitor = PdfReader(file)
    texto = ""


    for pagina in leitor.pages:
        texto += pagina.extract_text()

    texto = texto[:4000]

    prompt = f"""
    Resuma o texto abaixo em português, de forma clara e objetiva.
    Máximo de 20 linhas.

    Texto:
    {texto}
    """

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ],
)

    return response.choices[0].message.content 
