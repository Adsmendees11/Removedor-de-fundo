import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Removedor de Fundo", layout="centered")

st.title("Removedor de Fundo de Imagens")

imagem_upload = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if imagem_upload:
    imagem_bytes = imagem_upload.read()  # Lê os bytes uma única vez
    imagem = Image.open(io.BytesIO(imagem_bytes))  # Abre a imagem a partir dos bytes
    st.image(imagem, caption="Imagem Original", use_container_width=True)

    if st.button("Remover Fundo"):
        imagem_sem_fundo = remove(imagem_bytes)
        imagem_resultado = Image.open(io.BytesIO(imagem_sem_fundo))
        st.image(imagem_resultado, caption="Imagem Sem Fundo", use_container_width=True)

        st.download_button(
            label="📥 Baixar PNG com fundo transparente",
            data=imagem_sem_fundo,
            file_name="imagem_sem_fundo.png",
            mime="image/png"
        )