"""
Você deve criar uma classe carro que vai possuir dois atributos
compostos por duas classes:
1) Motor
O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
a) Atributo de dado velocidade
b) Método acelerar, que deverá incrementar a velocidade de uma unidade
c) Método freaer que deverá decrementar a velocidade em duas unidades
2) Direção
A direção terá a responsabilidade de controlar a direção. ela oferece
os seguintes atributos:
a) Valor de direção com valores  possíveis: norte, sul, leste, oeste
b) método girar_a_direita
c) método girar_a_esquerda

  N
O   L
  S

Exemplo:
# Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
# Testando Direção
>>> direção = Direção()
>>> direção.valor
'Norte'
>>> direção.girar_a_direita()
>>> direção.valor
'Leste'
>>> direção.girar_a_direita()
>>> direção.valor
'Sul'
>>> direção.girar_a_direita()
>>> direção.valor
'Oeste'
>>> direção.girar_a_direita()
>>> direção.valor
'Norte'
>>> direção.girar_a_esquerda()
>>> direção.valor
'Oeste'
>>> direção.girar_a_esquerda()
>>> direção.valor
'Sul'
>>> direção.girar_a_esquerda()
>>> direção.valor
'Leste'
>>> direção.girar_a_esquerda()
>>> direção.valor
'Norte'
>>> carro = Carro(direção, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> >>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> >>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> >>> carro.calcular_velocidade()
0
>>> carro.calcular_direção()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direção()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direção()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direção()
'Oeste'
"""
from motor import Motor
from direção import Direção


class Carro:
    def __init__(self, motor=Motor(), direção=Direção()):
        self.motor = motor
        self.direção = direção
        self.sentido = 'Norte'

    def girar_a_esquerda(self):
        self.sentido = self.direção.direcao_esquerda()

    def girar_a_direita(self):
        self.sentido = self.direção.girar_a_direita()

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def velocidade(self):
        print(self.motor.velocidade)
