
import streamlit as st
import random
from time import sleep

def simular_leitura_dht():
    temperatura = round(random.uniform(10, 60), 2)
    umidade = round(random.uniform(20, 90), 2)
    return temperatura, umidade

def simular_leitura_ultrassonico():
    return round(random.uniform(50, 150), 2)  # distância em cm

def simular_leitura_pir():
    return random.choice([True, False])

def simular_leitura_ldr():
    return random.randint(0, 300)  # luminosidade

def executar_fase_3():
    st.header("Fase 3 - Simulação de Sensores (Baseado no código C++)")

    if st.button("Executar Simulação"):
        temperatura, umidade = simular_leitura_dht()
        st.write(f"🌡️ Temperatura: {temperatura} °C")
        st.write(f"💧 Umidade: {umidade} %")

        if temperatura > 50 and umidade < 50:
            st.warning("⚠️ Condições extremas detectadas! Irrigação ativada.")

        distancia = simular_leitura_ultrassonico()
        st.write(f"📏 Distância (reservatório): {distancia} cm")
        if distancia > 100:
            st.warning("🚨 Nível de água baixo! Solicitada reposição de água.")

        movimento = simular_leitura_pir()
        if movimento:
            st.error("🚨 Movimento detectado! Sistema de alerta ativado.")
        else:
            st.success("✅ Nenhum movimento detectado.")

        luz = simular_leitura_ldr()
        st.write(f"💡 Nível de luminosidade: {luz} lux")
        if luz > 100:
            st.info("💧 Luminosidade alta! Irrigação ativada.")

        st.success("✅ Simulação finalizada.")
