from pprint import pprint

class Valvula():

    def __init__(self, abertura, vazao_fe = 0, vazao_25 = 0, vazao_50 = 0, vazao_75 = 0, vazao_ab = 0):
        self.abertura = abertura
        self.vazao_fe = vazao_fe
        self.vazao_25 = vazao_25
        self.vazao_50 = vazao_50
        self.vazao_75 = vazao_75
        self.vazao_ab = vazao_ab
        self.calcular_vazao()

    def calcular_vazao(self):
        if self.abertura <= 0:
            vazao =  self.vazao_fe
        if self.abertura <= 25 and self.abertura > 0:
            vazao =  ((self.vazao_25 - self.vazao_fe) / 25) * self.abertura
        if self.abertura <= 50 and self.abertura > 25:
            vazao =  self.vazao_25 + ((self.vazao_50 - self.vazao_25) / 25) * (self.abertura - 25)
        if self.abertura <= 75 and self.abertura > 50:
            vazao =  self.vazao_50 + ((self.vazao_75 - self.vazao_50) / 25) * (self.abertura - 50)
        if self.abertura < 100 and self.abertura > 75:
            vazao =  self.vazao_75 + ((self.vazao_ab - self.vazao_75) / 25) * (self.abertura - 75)
        if self.abertura >= 100:
            vazao =  self.vazao_ab
        self.vazao = round(vazao, 3)

    def imprimir_dados(self):
        pprint(vars(self))