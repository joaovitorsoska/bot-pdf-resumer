from dotenv import load_dotenv
import os
from langchain_community.chat_models import ChatOpenAI
from PyPDF2 import PdfReader

load_dotenv()

chat = ChatOpenAI(
    model="meta-llama/llama-3.1-8b-instruct",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)


def resumir_pdf(file):
    leitor = PdfReader(file)
    texto = ""


    for pagina in leitor.pages:
        texto += pagina.extract_text()

    prompt = f"""
    Resuma o texto abaixo em português, de forma clara e objetiva.
    Máximo de 20 linhas.

    Texto:
    {texto}
    """

    resposta = chat.invoke(prompt)
    return resposta.content