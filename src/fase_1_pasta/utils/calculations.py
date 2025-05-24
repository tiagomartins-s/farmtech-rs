import math

def calcular_area(quantidade_metro, quantidade):
    return 0 if quantidade_metro == 0 else quantidade / quantidade_metro

def calcular_area_largura_comprimento(largura, comprimento):
    return (largura * comprimento) / 10000

def calcular_quantidade(quantidade_metro, area):
    return area * quantidade_metro

def calcular_insumo(isumo_metro, area):
    return isumo_metro * area

def calcular_largura(area):
    return math.sqrt(area * 10000)

def calcular_comprimento(area):
    return math.sqrt(area * 10000)


def calcular_fileiras(largura, comprimento, espacamento):
    resto_largura = largura % espacamento
    resto_comprimento = comprimento % espacamento

    if resto_largura < resto_comprimento:
        fileiras = largura // espacamento
    elif resto_comprimento < resto_largura:
        fileiras = comprimento // espacamento
    elif largura < comprimento:
        fileiras = largura // espacamento
    else:
        fileiras = comprimento // espacamento

    return fileiras