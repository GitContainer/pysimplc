from random import randint
from pprint import pprint

class Poco():

    def __init__(self, vazao_oleo, vazao_agua, vazao_gas, regularidade_fluxo = 1.0):
        self.vazao_oleo = vazao_oleo
        self.vazao_agua = vazao_agua
        self.vazao_gas = vazao_gas
        self.regularidade_fluxo = regularidade_fluxo
        self.calcular_fluxo()

    def calcular_fluxo(self):
        fluxo = {'oleo':0.0, 'agua':0.0, 'gas':0.0}
        fluxo['oleo'] = self.vazao_oleo + self.gerar_irregularidade(self.vazao_oleo)
        fluxo['agua'] = self.vazao_agua + self.gerar_irregularidade(self.vazao_agua)
        fluxo['gas'] = self.vazao_gas + self.gerar_irregularidade(self.vazao_gas)
        self.fluxo = fluxo

    def gerar_irregularidade(self, valor_referencia):
        limite_inferior = -1 * valor_referencia * abs(self.regularidade_fluxo - 1)
        limite_superior = valor_referencia * abs(self.regularidade_fluxo - 1)
        irregularidade = randint(int(limite_inferior), int(limite_superior))
        return irregularidade

    def imprimir_dados(self):
        pprint(vars(self))