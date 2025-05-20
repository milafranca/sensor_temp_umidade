import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db

st.set_page_config(page_title="Dashboard IoT", layout="centered")
st.title("️Dashboard de Temperatura e Umidade")

if not firebase_admin._apps:
    cred = credentials.Certificate("credenciais.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://iot-monitor-5ca0c-default-rtdb.firebaseio.com/"
    })

# Busca dados
ref = db.reference("leituras")
dados = ref.get()

if dados:
    df = pd.DataFrame(dados).T
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values('timestamp')

    st.line_chart(df[["temperatura", "umidade"]].set_index(df["timestamp"]))
    st.dataframe(df[["timestamp", "temperatura", "umidade"]])
else:
    st.warning("Nenhum dado encontrado no Firebase.")



