import streamlit as st
import sqlite3
from datetime import datetime
from random import uniform

DB_PATH = 'fase2.db'

# Inicialização do banco
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temperatura (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            valor REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS umidade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            valor REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            mensagem TEXT
        )
    """)
    conn.commit()
    conn.close()

def record_log(mensagem):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO logs (data_hora, mensagem) VALUES (?, ?)", (str(datetime.now()), mensagem))

def view_log():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT * FROM logs").fetchall()

def insert_temperature(valor):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO temperatura (data_hora, valor) VALUES (?, ?)", (str(datetime.now()), valor))

def insert_humidity(valor):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO umidade (data_hora, valor) VALUES (?, ?)", (str(datetime.now()), valor))

def last_temperature():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT data_hora, valor FROM temperatura ORDER BY id DESC LIMIT 1").fetchone()

def last_humidity():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT data_hora, valor FROM umidade ORDER BY id DESC LIMIT 1").fetchone()

def clear_base():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM temperatura")
        conn.execute("DELETE FROM umidade")
        conn.execute("DELETE FROM logs")

def check_temperature(temp):
    if temp is None:
        return "Sem dados"
    if 18 <= temp <= 25:
        return "Temperatura adequada"
    return "Temperatura fora do ideal"

def check_humidity(umid):
    if umid is None:
        return "Sem dados"
    if 40 <= umid <= 70:
        return "Umidade adequada"
    return "Umidade fora do ideal"

def status():
    temp = last_temperature()
    umid = last_humidity()
    return check_temperature(temp[1] if temp else None), check_humidity(umid[1] if umid else None)

def generate_test_data():
    with sqlite3.connect(DB_PATH) as conn:
        for _ in range(1000):
            conn.execute("INSERT INTO temperatura (data_hora, valor) VALUES (?, ?)", (str(datetime.now()), round(uniform(15, 30), 2)))
            conn.execute("INSERT INTO umidade (data_hora, valor) VALUES (?, ?)", (str(datetime.now()), round(uniform(35, 75), 2)))
        conn.commit()

def generate_report():
    with sqlite3.connect(DB_PATH) as conn:
        temperaturas = conn.execute("SELECT * FROM temperatura ORDER BY id DESC LIMIT 5").fetchall()
        umidades = conn.execute("SELECT * FROM umidade ORDER BY id DESC LIMIT 5").fetchall()
        total = conn.execute("SELECT COUNT(*) FROM temperatura").fetchone()[0]
    return {
        "total leituras": total,
        "temperaturas": temperaturas,
        "umidades": umidades
    }

def executar_fase_2():
    init_db()
    st.header("Fase 2 - Sistema de Irrigação com SQLite")

    opcoes = [
        "Cadastrar dados sensores",
        "Verificar status plantação",
        "Gerar relatório",
        "Ver logs",
        "Gerar dados teste",
        "Limpar base"
    ]

    escolha = st.selectbox("Escolha uma opção:", opcoes)

    if escolha == opcoes[0]:
        temp = st.number_input("Temperatura (°C):", step=0.1, format="%.2f")
        umid = st.number_input("Umidade (%):", step=0.1, format="%.2f")
        if st.button("Salvar"):
            insert_temperature(temp)
            insert_humidity(umid)
            record_log(f"Dados inseridos: Temp={temp}, Umidade={umid}")
            st.success("Dados salvos com sucesso.")

    elif escolha == opcoes[1]:
        temp_status, umid_status = status()
        st.write(f"Status Temperatura: {temp_status}")
        st.write(f"Status Umidade: {umid_status}")

    elif escolha == opcoes[2]:
        relatorio = generate_report()
        st.json(relatorio)

    elif escolha == opcoes[3]:
        logs = view_log()
        for log in logs:
            st.text(f"{log[1]} - {log[2]}")

    elif escolha == opcoes[4]:
        if st.button("Gerar dados teste"):
            generate_test_data()
            st.success("Dados de teste gerados.")

    elif escolha == opcoes[5]:
        if st.button("Limpar base de dados"):
            clear_base()
            st.success("Base de dados limpa.")
