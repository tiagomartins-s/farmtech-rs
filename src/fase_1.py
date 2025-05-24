import streamlit as st
from datetime import datetime
from openpyxl import Workbook
from utils.calculations import calcular_area_largura_comprimento
from cultures.grape import Grape
from cultures.soybean import Soybean
import os

culturas_disponiveis = {'Uva': Grape, 'Soja': Soybean}
opcoes_calculo = ["Quantidade desejada de colheita", "Área de plantio"]
dados_culturas = []

def exportar_dados_para_xlsx(cultura_nome, dados_filtrados):
    os.makedirs('ProjectR', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f"ProjectR/{cultura_nome}_dados_culturas_{timestamp}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = cultura_nome

    cabecalhos = ["Cultura", "Área", "Largura", "Comprimento", "Quantidade", "Fileiras"]
    for insumo in dados_filtrados[0]['insumos']:
        cabecalhos.append(insumo['nome'])

    ws.append(cabecalhos)

    for dado in dados_filtrados:
        linha = [dado["cultura"], dado["area"], dado["largura"], dado["comprimento"], dado["quantidade"], dado["fileiras"]]
        for insumo in dado["insumos"]:
            linha.append(insumo["quantidade"])
        ws.append(linha)

    wb.save(nome_arquivo)
    return nome_arquivo

def executar_fase_1():
    st.header("Fase 1 - Gestão de Culturas Agrícolas")

    menu = st.sidebar.selectbox("Menu", [
        "Inserir Dados", "Visualizar Dados", "Atualizar Dados",
        "Deletar Dados", "Exportar para Excel"
    ])

    if menu == "Inserir Dados":
        cultura_nome = st.selectbox("Escolha a Cultura", list(culturas_disponiveis.keys()))
        cultura_classe = culturas_disponiveis[cultura_nome]
        tipo_entrada = st.selectbox("Tipo de Entrada", opcoes_calculo)

        if tipo_entrada == "Quantidade desejada de colheita":
            quantidade = st.number_input("Quantidade que deseja colher (Kg)", min_value=0.0, step=1.0)
            if st.button("Inserir"):
                cultura = cultura_classe(quantidade=quantidade)
                dados_culturas.append({
                    "cultura": cultura.nome,
                    "area": cultura.area,
                    "largura": cultura.largura,
                    "comprimento": cultura.comprimento,
                    "quantidade": cultura.quantidade,
                    "fileiras": cultura.fileiras,
                    "insumos": cultura.insumos_necessarios
                })
                st.success("Dados inseridos com sucesso!")

        elif tipo_entrada == "Área de plantio":
            largura = st.number_input("Largura da área (m)", min_value=0.0)
            comprimento = st.number_input("Comprimento da área (m)", min_value=0.0)
            if st.button("Inserir"):
                area = calcular_area_largura_comprimento(largura, comprimento)
                cultura = cultura_classe(area=area, largura=largura, comprimento=comprimento)
                dados_culturas.append({
                    "cultura": cultura.nome,
                    "area": cultura.area,
                    "largura": cultura.largura,
                    "comprimento": cultura.comprimento,
                    "quantidade": cultura.quantidade,
                    "fileiras": cultura.fileiras,
                    "insumos": cultura.insumos_necessarios
                })
                st.success("Dados inseridos com sucesso!")

    elif menu == "Visualizar Dados":
        if not dados_culturas:
            st.warning("Nenhum dado disponível.")
        else:
            for i, dado in enumerate(dados_culturas):
                st.markdown(f"### {i+1}. Cultura: {dado['cultura']}")
                st.write(f"Área: {dado['area']:.4f} ha")
                st.write(f"Largura: {dado['largura']:.2f} m")
                st.write(f"Comprimento: {dado['comprimento']:.2f} m")
                st.write(f"Colheita: {dado['quantidade']:.2f} Kg")
                st.write(f"Fileiras: {dado['fileiras']}")
                for insumo in dado["insumos"]:
                    st.write(f"{insumo['nome']}: {insumo['quantidade']:.2f} {insumo['unidade_medida']}")

    elif menu == "Atualizar Dados":
        if not dados_culturas:
            st.warning("Nenhum dado para atualizar.")
        else:
            index = st.number_input("Número do dado a atualizar", min_value=1, max_value=len(dados_culturas)) - 1
            cultura_nome = dados_culturas[int(index)]["cultura"]
            cultura_classe = culturas_disponiveis[cultura_nome]
            tipo_entrada = st.selectbox("Novo tipo de entrada", opcoes_calculo)

            if tipo_entrada == "Quantidade desejada de colheita":
                quantidade = st.number_input("Nova quantidade (Kg)", min_value=0.0)
                if st.button("Atualizar"):
                    cultura = cultura_classe(quantidade=quantidade)
                    dados_culturas[int(index)] = {
                        "cultura": cultura.nome,
                        "area": cultura.area,
                        "largura": cultura.largura,
                        "comprimento": cultura.comprimento,
                        "quantidade": cultura.quantidade,
                        "fileiras": cultura.fileiras,
                        "insumos": cultura.insumos_necessarios
                    }
                    st.success("Dados atualizados com sucesso!")

            elif tipo_entrada == "Área de plantio":
                largura = st.number_input("Nova largura (m)", min_value=0.0)
                comprimento = st.number_input("Novo comprimento (m)", min_value=0.0)
                if st.button("Atualizar"):
                    area = calcular_area_largura_comprimento(largura, comprimento)
                    cultura = cultura_classe(area=area, largura=largura, comprimento=comprimento)
                    dados_culturas[int(index)] = {
                        "cultura": cultura.nome,
                        "area": cultura.area,
                        "largura": cultura.largura,
                        "comprimento": cultura.comprimento,
                        "quantidade": cultura.quantidade,
                        "fileiras": cultura.fileiras,
                        "insumos": cultura.insumos_necessarios
                    }
                    st.success("Dados atualizados com sucesso!")

    elif menu == "Deletar Dados":
        if not dados_culturas:
            st.warning("Nenhum dado para deletar.")
        else:
            index = st.number_input("Número do dado a deletar", min_value=1, max_value=len(dados_culturas)) - 1
            if st.button("Deletar"):
                del dados_culturas[int(index)]
                st.success("Dado deletado com sucesso!")

    elif menu == "Exportar para Excel":
        if not dados_culturas:
            st.warning("Nenhum dado para exportar.")
        else:
            cultura_nome = st.selectbox("Cultura a exportar", list(culturas_disponiveis.keys()))
            dados_filtrados = [d for d in dados_culturas if d['cultura'] == cultura_nome]
            if st.button("Exportar"):
                arquivo = exportar_dados_para_xlsx(cultura_nome, dados_filtrados)
                st.success(f"Exportado com sucesso: {arquivo}")
