import streamlit as st
from fase_1 import executar_fase_1
from fase_2 import executar_fase_2
from fase_3 import executar_fase_3
from fase_4 import executar_fase_4 
from fase_5 import executar_fase_5
from fase_6 import executar_fase_6



st.set_page_config(page_title="Sistema de Irrigação Inteligente - Gestão Agrícola", layout="wide")
st.title("Sistema de Irrigação Inteligente - Gestão Agrícola")

fase_selecionada = st.sidebar.selectbox(
    "Selecione o Projeto (Fase)",
    ["", "Fase 1", "Fase 2", "Fase 3", "Fase 4", "Fase 5", "Fase 6"]
)

if fase_selecionada == "Fase 1":
    executar_fase_1()
if fase_selecionada == "Fase 2":
    executar_fase_2()
if fase_selecionada == "Fase 3":
    executar_fase_3()
elif fase_selecionada == "Fase 4":
    executar_fase_4()
elif fase_selecionada == "Fase 5":
    executar_fase_5()
elif fase_selecionada == "Fase 6":
    executar_fase_6()
else:
    st.write("### Por favor, selecione uma fase no menu lateral para acessar as funcionalidades.")
