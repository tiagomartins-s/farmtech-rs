from cultures.base_culture import BaseCulture

class Grape(BaseCulture):
    def __init__(self, quantidade=None, area=None, largura = None, comprimento = None):
        insumos = [
            {"nome": "Mancozebe", "unidade_medida": "Kg", "quantidade_ha": 2.16},
            {"nome": "Sulfato de cobre", "unidade_medida": "Kg", "quantidade_ha": 7.2},
            {"nome": "Água", "unidade_medida": "Litros", "quantidade_ha": 720}
        ]
        super().__init__("Uva", 16000, 2.5, quantidade=quantidade, area=area,
                         largura = largura, comprimento = comprimento, insumos=insumos)
