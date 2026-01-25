import os
from langchain_community.chat_models import ChatOpenAI
from PyPDF2 import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

API_key = "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"
os.environ["OPENAI_API_KEY"] = API_key

chat = ChatOpenAI(
    model= "meta-llama/llama-3.1-8b-instruct",
    openai_api_key= API_key,
    openai_api_base= "https://openrouter.ai/api/v1",
)


nltk.download("punkt")
nltk.download("stopwords")

def resumir_pdf(caminho_pdf):
    leitor = PdfReader(caminho_pdf)
    texto = ""

    
    for pagina in leitor.pages:
        texto += pagina.extract_text()

    prompt = f"""
    Resuma o texto abaixo EM PORTUGUÊS, de forma clara e objetiva.
    Mesmo que o texto original esteja em outro idioma, o resumo deve ser em português.

    Texto:
    {texto}
    """

    resposta = chat.invoke(prompt)
    return resposta.content


    return "\n".join(resumo)


print(" Bem vindo! SKbot iniciado")
print(" Se precisar, digite 'Sair' para encerrar o chat.")

sistema_chat = " Você é um chat bot chamado SKbot e responde em portugês. Seja sempre educado nas respostas." \
 

sistema_resumo = "O resumo precisa ser sempre em português e no máximo de 20 linhas."

memoria_bot = []

while True:
    pergunta = input("\nUsuário: ").strip()

    if pergunta =="":
        print("Digite algo válido.")
        continue
   
    if pergunta.lower() == "sair":
        print(" O chat foi encerrado. Até a próxima!")
        break

    if pergunta.lower().startswith("resumir"):
        try:
             nome_arquivo = pergunta.split(" ", 1)[1]
             resumo = resumir_pdf(nome_arquivo)
             print("SKbot (Resumo do PDF):\n", resumo)
        except Exception as e:
             print("Erro ao resumir o PDF:", e)
        continue



    texto_memoria = "".join(memoria_bot)


    print("Pensando...")

    resposta = chat.invoke(sistema_chat + texto_memoria + pergunta + sistema_resumo)
    print(f"SKbot: {resposta.content}")

    memoria_bot.append("Você: " + pergunta + "\n")
    memoria_bot.append("SKbot: " + resposta.content + "\n")

    while len(memoria_bot) > 4:
        memoria_bot.pop(0)
    


    



