from cultures.base_culture import BaseCulture

class Soybean(BaseCulture):
    def __init__(self, quantidade=None, area=None, largura = None, comprimento = None):
        insumos = [
            {"nome": "Sementes", "unidade_medida": "Kg", "quantidade_ha": 50},
            {"nome": "Adubo", "unidade_medida": "Kg", "quantidade_ha": 300}
        ]
        super().__init__("Soja", 3600, 0.5, quantidade=quantidade,
                         area=area,  largura = largura, comprimento = comprimento, insumos=insumos)
