from pycomm.ab_comm.clx import Driver as ClxDriver
from pycomm.ab_comm.slc import Driver as SlcDriver
from math import floor
from time import sleep

class Simulador():

    DEBUG = True

    def __init__(self, plc='clx', ip='0.0.0.0'):
        if plc == 'clx':
            self.driver = ClxDriver()
        if plc =='slc':
            self.driver = SlcDriver()
        self.ip = ip
        self.open()

    def open(self):
        try: self.driver.open(self.ip)
        except: self.error(0)
        else: return True
            
    def error(self, code):
        if code == 0:
            self.log('Could not connect to IP')
    
    def log(self, message):
        if self.DEBUG == True:
            print(message)
        with open('log', 'w') as f:
            f.write(message)
            f.close()

    def simular(self, time_step=1):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.days = 0

        while True:
            exec_start = time()
            print(self.step_clock(1))


            delta = time() - exec_start
            self.wait_step(delta, time_step)
    
    def step_clock(self, step):
        self.seconds += step
        if self.seconds >= 60:
            self.minutes += floor(self.seconds / 60)
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += floor(self.minutes / 60)
            self.minutes = self.minutes % 60
        if self.hours >= 24:
            self.days += floor(self.hours / 24)
            self.hours = self.hours % 24
        return (self.days, self.hours, self.minutes, self.seconds)
    
    def wait_step(self, delta, step):
        if delta > step:
            self.error(1)
            return False
        sleep(step-delta)

    # funcao para transformar inteiro em array de binarios
    def formatar_binario(self, inteiro, numero_bits):
        b = []
        if numero_bits == 32:
            for n in '{0:032b}'.format(inteiro):
                b.append(int(n))
        if numero_bits == 16:
            for n in '{0:016b}'.format(inteiro):
                b.append(int(n))
        b.reverse()
        return b

    # funcao para transformar array de binarios em inteiro
    def formatar_inteiro(self, array_binario):
        array_binario.reverse()
        binario = ''
        for b in array_binario:
            binario = binario + str(b)
        decimal = 0
        for digito in binario:
            decimal = decimal * 2 + int(digito)
        return decimal


if __name__ == '__main__':
    sim = Simulador()
    sim.simular()