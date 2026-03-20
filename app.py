import streamlit as st
import requests
import random
import string

WEBHOOK_URL = "https://hook.us2.make.com/pge18s5nwbpciprxph4o1yokco3a"

def generar_token():
    return ''.join(random.choices(string.digits, k=6))

st.title("Portal de Proveedores")

cuit = st.text_input("Ingresá tu CUIT")

if st.button("Solicitar acceso"):
    if cuit:
        token = generar_token()

        payload = {
            "cuit": cuit,
            "token": token
        }

        response = requests.post(WEBHOOK_URL, json=payload)

        st.success("Te enviamos un código por mail 📩")
    else:
        st.error("Ingresá un CUIT válido")
