from math import pi, acos, sqrt
from pprint import pprint

class Separador():

    def __init__(self, raio, comprimento, distancia_vertedouro, altura_vertedouro, nivel_liquido = 0, nivel_agua = 0, nivel_oleo = 0, pressao = 100):
        self.raio = raio
        self.comprimento = comprimento
        self.distancia_vertedouro = distancia_vertedouro
        self.altura_vertedouro = altura_vertedouro
        self.nivel_liquido = nivel_liquido
        self.nivel_agua = nivel_agua
        self.nivel_oleo = nivel_oleo
        self.pressao = pressao
        self.volume_maximo = self.calcular_volume_maximo()
        self.volume_maximo_liquido = self.calcular_volume_liquido(1, 100.0)
        self.volume_maximo_oleo = self.calcular_volume_liquido(3, 100.0)
        self.calcular_volumes()

    def calcular_volumes(self):
        self.volume_liquido = self.calcular_volume_liquido(1, self.nivel_liquido)
        self.volume_agua = self.calcular_volume_liquido(2, self.nivel_agua)
        self.volume_oleo_camara_1 = round(self.volume_liquido - self.volume_agua, 5)
        self.volume_oleo_camara_2 = self.calcular_volume_liquido(3, self.nivel_oleo)
        self.volume_oleo = round(self.volume_oleo_camara_1 + self.volume_oleo_camara_2, 5)
        self.volume_gas = self.calcular_volume_gas()

    def calcular_niveis(self):
        self.nivel_liquido = self.calcular_nivel_liquido(1, self.volume_liquido)
        self.nivel_agua = self.calcular_nivel_liquido(2, self.volume_agua)
        self.nivel_oleo = self.calcular_nivel_liquido(3, self.volume_oleo_camara_2)

    def calcular_pressao(self):
        self.pressao = round((self.volume_gas / (self.volume_maximo - (self.volume_agua + self.volume_oleo))) * 100, 5)

    def calcular_volume_maximo(self):
        volume_maximo = pi * (self.raio ** 2.0) * self.comprimento
        return round(volume_maximo, 3)

    def calcular_volume_liquido(self, fluido, nivel):
        altura_nivel = (nivel / 100.0) * ((2.0 * self.raio) - self.altura_vertedouro) 
        area_circulo = pi * (self.raio ** 2.0)
        area_setor = (self.raio ** 2.0) * acos((self.raio - altura_nivel) / self.raio)
        area_triangulo = (self.raio - altura_nivel) * sqrt((2.0 * self.raio * altura_nivel) - (altura_nivel ** 2.0))
        area_liquido = area_circulo - (area_circulo - area_setor + area_triangulo)
        if fluido == 2 or fluido == 1: # fluido 1 = agua + oleo, fluido 2 = agua
            volume_total_liquido = area_liquido * self.distancia_vertedouro
        if fluido == 3: # fluido 3 = oleo
            volume_total_liquido = area_liquido * (self.comprimento - self.distancia_vertedouro)
        return  round(volume_total_liquido, 5)
    
    def calcular_volume_gas(self):
        volume_gas = (self.volume_maximo - (self.volume_agua + self.volume_oleo)) * (self.pressao / 100.0)
        return round(volume_gas, 5)


    def calcular_nivel_liquido(self, fluido, volume):
        if fluido == 3:
            a = volume / ((self.comprimento - self.distancia_vertedouro) * (self.raio ** 2.0))
        if fluido == 2 or fluido == 1:
            a = volume / (self.distancia_vertedouro * (self.raio ** 2.0))
        
        nivel = (8.0*a - sqrt(pi) * (sqrt((pi-4.0) * ((pi-2.0*a)**2.0) + 4.0*pi)) - (2.0*pi) * (a+1.0) + (pi**2.0)) / ((pi-4.0) * (pi - (2.0*a)))
        
        
        return round(nivel * 100, 5)

    def imprimir_dados(self):
        pprint(vars(self))