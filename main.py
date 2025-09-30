# Titulo
# Input do chat
# A cada mensagem enviada
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# Streamlit - ferramenta para criar site, principalmente para criar interações com IA
    # Front e Back

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="")

st.write("# Chatbot com IA")

# session_state= memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exbir o historico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")
if mensagem_usuario:
    
    # user -> ser humano
    # assistant -> IA
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)


    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content
    
    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)