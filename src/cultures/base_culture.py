from utils.calculations import calcular_area, calcular_insumo, calcular_quantidade, calcular_largura, calcular_comprimento, calcular_fileiras

class BaseCulture:
    def __init__(self, nome, quantidade_ha, espacamento_fileiras_m, quantidade=None, area=None, largura = None,
                 comprimento = None, insumos=None):
        self.nome = nome
        self.quantidade_ha = quantidade_ha
        self.espacamento_fileiras_m = espacamento_fileiras_m
        self.insumos_necessarios = []

        if quantidade is not None:
            self.quantidade = quantidade
            self.area = calcular_area(self.quantidade_ha, self.quantidade)
            self.largura = calcular_largura(self.area)
            self.comprimento = calcular_comprimento(self.area)
            self.fileiras = calcular_fileiras(self.largura, self.comprimento, self.espacamento_fileiras_m)
        elif area is not None:
            self.area = area
            self.largura = largura
            self.comprimento = comprimento
            self.fileiras = calcular_fileiras(self.largura, self.comprimento, self.espacamento_fileiras_m)
            self.quantidade = calcular_quantidade(self.quantidade_ha, self.area)
        else:
            raise ValueError("Você deve fornecer 'quantidade' ou 'area'.")

        if insumos:
            for insumo in insumos:
                self.insumos_necessarios.append({
                    "nome": insumo["nome"],
                    "unidade_medida": insumo["unidade_medida"],
                    "quantidade": calcular_insumo(insumo["quantidade_ha"], self.area)
                })



