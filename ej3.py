#! /usr/bin/python
from math import sqrt

def input_coeficientes():
    a = int(input('Coeficiente A: '))
    b = int(input('Coeficiente B: '))
    c = int(input('Coeficiente C: '))

    return a, b, c

def mostrar_raices(r1, r2):
    print('Raiz 1: {}'.format(r1))
    print('Raiz 2: {}'.format(r2))

def formula_general(a, b, c):
    numerador_positivo = -b + sqrt((b ** 2) - (4 * a * c))
    numerador_negativo = -b - sqrt((b ** 2) - (4 * a * c))
    denominador = 2 * a

    raiz1 = numerador_positivo / denominador
    raiz2 = numerador_negativo / denominador

    return raiz1, raiz2

a, b, c = input_coeficientes()
r1, r2 = formula_general(a, b, c)
mostrar_raices(r1, r2)
