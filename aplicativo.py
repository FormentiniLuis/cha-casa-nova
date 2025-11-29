import streamlit as st
import pandas as pd
import os

CSV_PATH = "lista_presente_casa_nova.csv"
IMG_PATH = "dudu2.webp"   # coloque aqui o nome EXATO do arquivo da imagem

st.set_page_config(page_title="Lista de Presentes — Casa Nova", page_icon="🏡")

# Imagem no topo
if os.path.exists(IMG_PATH):
    st.image(IMG_PATH, width=300)
else:
    st.warning(f"Imagem '{IMG_PATH}' não encontrada. Coloque o arquivo na mesma pasta do app.")

st.title("🏡 Lista de Presentes — Chá de Casa Nova")
st.write("Selecione um presente para o Luís. Após escolher, o item ficará indisponível para outras pessoas.")

# --- Carregar CSV ---
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
else:
    st.error("Arquivo CSV não encontrado!")
    st.stop()

# --- Filtrar itens disponíveis ---
df_disponiveis = df[df["selecionado"] == "não"]

if df_disponiveis.empty:
    st.success("🎉 Todos os presentes já foram escolhidos!")
    st.stop()

# --- Seleção ---
opcao = st.selectbox(
    "Escolha um presente disponível:",
    df_disponiveis["item"].tolist()
)

nome = st.text_input("Seu nome (opcional):")

if st.button("Confirmar escolha"):
    df.loc[df["item"] == opcao, "selecionado"] = "sim" if nome.strip() == "" else f"sim — {nome}"

    df.to_csv(CSV_PATH, index=False)

    st.success(f"Obrigado! O item **{opcao}** foi reservado por você.")
    st.balloons()
    st.rerun()
