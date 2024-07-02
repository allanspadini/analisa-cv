import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from PyPDF2 import PdfReader


def get_response(text):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Analise o curriculum a seguir e retorne pontos de melhoria: {text}",
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content



def main():

    load_dotenv()
    

    st.title("Analisador de CV da Claridy")
    # Widget para upload do arquivo
    uploaded_file = st.file_uploader("Escolha um arquivo PDF", type=["pdf"])

    if uploaded_file is not None:
    
        pdf_reader = PdfReader(uploaded_file)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        st.success("Arquivo PDF carregado com sucesso!")
        st.markdown(get_response(text))  # Exibe o texto extraído
        

    



if __name__ == "__main__":
    main()
