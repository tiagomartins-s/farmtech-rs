import os
from datetime import datetime
from openpyxl import Workbook
from cultures.grape import Grape
from cultures.soybean import Soybean
from utils.calculations import calcular_area_largura_comprimento

culturas_disponiveis = {'Uva': Grape, 'Soja': Soybean}
opcoes_calculo = ["Quantidade desejada de colheita", "Área de plantio"]
dados_culturas = []


def escolher_cultura():
    print("Culturas disponíveis:")
    for i, cultura in enumerate(culturas_disponiveis.keys()):
        print(f"{i + 1}. {cultura}")
    escolha = int(input("Escolha o número da cultura: "))
    while 0 >= escolha or escolha > len(culturas_disponiveis):
        escolha = int(input("Cultura inválida. Tente novamente: "))
    cultura_selecionada = list(culturas_disponiveis.keys())[escolha - 1]
    return culturas_disponiveis[cultura_selecionada]


def escolher_opcao_calculo():
    print("Escolha a informação de entrada:")
    for i, opcao in enumerate(opcoes_calculo):
        print(f"{i + 1}. {opcao}")
    escolha = int(input("Escolha o número da opção: "))
    while 0 >= escolha or escolha > len(opcoes_calculo):
        escolha = int(input("Opção inválida. Tente novamente: "))
    return escolha - 1


def popular_dados_cultura(cultura_classe, opcao_escolhida):
    if opcao_escolhida == 0:  # Quantidade
        quantidade = float(input("Digite a quantidade que deseja colher em Kg: "))
        while 0 >= quantidade:
            quantidade = float(input("A quantidade deve ser maior que 0: "))
        cultura = cultura_classe(quantidade=quantidade)
    else: # Área
        largura = float(input("Digite a largura da área mestros: "))
        while 0 >= largura:
            largura = float(input("A largura deve ser maior que 0: "))

        comprimento = float(input("Digite o comprimento da área em metros: "))
        while 0 >= comprimento:
            comprimento = float(input("O comprimento deve ser maior que 0: "))

        area = calcular_area_largura_comprimento(largura, comprimento)

        cultura = cultura_classe(area=area, largura=largura, comprimento=comprimento)

    return cultura


def inserir_dados():
    cultura_classe = escolher_cultura()
    opcao_escolhida = escolher_opcao_calculo()
    cultura = popular_dados_cultura(cultura_classe, opcao_escolhida)
    dados_culturas.append({
        "cultura": cultura.nome,
        "area": cultura.area,
        "largura": cultura.largura,
        "comprimento": cultura.comprimento,
        "quantidade": cultura.quantidade,
        "fileiras": cultura.fileiras,
        "insumos": cultura.insumos_necessarios
    })
    print("Dados inseridos com sucesso!")


def mostrar_dados():
    for i, dado in enumerate(dados_culturas):
        print(
            f"{i + 1}. Cultura: {dado['cultura']:20} \n"
            f" Área em hectares: {dado['area']:,.4f} \n"
            f" Largura em metros: {dado['largura']:,.4f} \n"
            f" Comprimento em metros: {dado['comprimento']:,.4f} \n"
            f" Colheita em Kg: {dado['quantidade']:,.4f} \n"
            f" Fileiras: {dado['fileiras']:,}"
        )
        for insumo in dado["insumos"]:
            print(
                f" {insumo['nome']} em {insumo['unidade_medida']}: {insumo['quantidade']:,.4f}"
            )
        print()  # Adiciona uma linha em branco entre culturas

def atualizar_dados():
    mostrar_dados()
    index = int(input("Escolha o número do dado que deseja atualizar: ")) - 1
    if 0 <= index < len(dados_culturas):
        cultura_classe = culturas_disponiveis[dados_culturas[index]["cultura"]]
        opcao_escolhida = escolher_opcao_calculo()
        cultura = popular_dados_cultura(cultura_classe, opcao_escolhida)
        dados_culturas[index] = {
            "cultura": cultura.nome,
            "area": cultura.area,
            "largura": cultura.largura,
            "comprimento": cultura.comprimento,
            "quantidade": cultura.quantidade,
            "fileiras": cultura.fileiras,
            "insumos": cultura.insumos_necessarios
        }
        print("Dados atualizados com sucesso!")
    else:
        print("Índice inválido.")


def deletar_dados():
    mostrar_dados()
    index = int(input("Escolha o número do dado que deseja deletar: ")) - 1
    if 0 <= index < len(dados_culturas):
        del dados_culturas[index]
        print("Dados deletados com sucesso!")
    else:
        print("Índice inválido.")


def exportar_dados_para_xlsx():
    cultura_classe = escolher_cultura()

    cultura_selecionada_nome = None
    for nome, classe in culturas_disponiveis.items():
        if classe == cultura_classe:
            cultura_selecionada_nome = nome
            break

    if cultura_selecionada_nome is None:
        print("Cultura não encontrada.")
        return

    dados_filtrados = [
        dado for dado in dados_culturas
        if dado['cultura'] == cultura_selecionada_nome
    ]

    if not dados_filtrados:
        print("Nenhum dado encontrado para a cultura selecionada.")
        return

    os.makedirs('ProjectR', exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f"ProjectR/{cultura_selecionada_nome}_dados_culturas_{timestamp}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = cultura_selecionada_nome

    cabecalhos = ["Cultura", "Área", "Largura", "Comprimento", "Quantidade", "Fileiras"]
    for insumo in dados_filtrados[0]['insumos']:
        cabecalhos.append(insumo['nome'])

    ws.append(cabecalhos)

    for dado in dados_filtrados:
        linha = [dado["cultura"], dado["area"], dado["largura"], dado["comprimento"], dado["quantidade"]
            , dado["fileiras"]]
        for insumo in dado["insumos"]:
            linha.append(insumo["quantidade"])
        ws.append(linha)

    wb.save(nome_arquivo)
    print(f"Dados exportados com sucesso para {nome_arquivo}")
