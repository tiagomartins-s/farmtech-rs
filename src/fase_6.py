
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import time

# Carrega o modelo YOLOv5s (baixado automaticamente se não existir)
model = YOLO('yolov5s.pt')

def detectar_objetos(imagem_path):
    results = model(imagem_path)
    results[0].save(filename='saida.jpg')  # salva imagem com anotações
    return 'saida.jpg', results[0].boxes.data.cpu().numpy()

def executar_fase_6():
    st.header("Fase 6 - Detecção de Objetos com YOLOv5 (via ultralytics lib)")

    uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        os.makedirs("temp_upload", exist_ok=True)
        imagem_path = os.path.join("temp_upload", uploaded_file.name)

        with open(imagem_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(imagem_path, caption="Imagem original", use_container_width=True)

        if st.button("Detectar objetos"):
            with st.spinner("Detectando..."):
                imagem_saida, detections = detectar_objetos(imagem_path)
                st.image(imagem_saida, caption="Objetos detectados", use_container_width=True)
                st.subheader("Detecções (caixas):")
                st.write(detections)
