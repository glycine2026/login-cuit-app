import streamlit as st
import requests
import random
import string
from datetime import datetime, timedelta

# memoria temporal (solo demo)
if "tokens" not in st.session_state:
    st.session_state.tokens = {}

def generar_token():
    return ''.join(random.choices(string.digits, k=6))

def guardar_token(cuit, token):
    st.session_state.tokens[cuit] = {
        "token": token,
        "expira": datetime.now() + timedelta(minutes=10)
    }

def validar_token(cuit, token):
    data = st.session_state.tokens.get(cuit)
    if not data:
        return False
    if datetime.now() > data["expira"]:
        return False
    return data["token"] == token

def enviar_a_make(cuit, token):
    url = "https://hook.us2.make.com/pge18s5nwbpciprxph4o1yokco3a"
    requests.post(url, json={"cuit": cuit, "token": token})

st.title("Login con CUIT")

cuit = st.text_input("Ingresá tu CUIT")

if st.button("Enviar token"):
    token = generar_token()
    guardar_token(cuit, token)
    enviar_a_make(cuit, token)
    st.success("Te enviamos un token por mail")

st.divider()

token_input = st.text_input("Ingresá el token")

if st.button("Ingresar"):
    if validar_token(cuit, token_input):
        st.success("Acceso concedido 🎉")
        st.write("Bienvenido al panel")
    else:
        st.error("Token inválido o expirado")
