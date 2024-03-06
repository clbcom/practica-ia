#! /usr/bin/python

from math import pi

# a) funcion sin parametros y que no retorna valores
def cilindro_a():
    r = int(input('Ingrese el radio: '))
    h = int(input('Ingrese la altura: '))

    area = pi * (r ** 2) * h
    volumen = 2 * pi * r * (r + h)

    print('El area es: {}'.format(area))
    print('El volumen es: {}'.format(volumen))

# b) funcion con parametros y que no retorna ningun valor
def cilindro_b(r, h):
    area = pi * (r ** 2) * h
    volumen = 2 * pi * r * (r + h)

    print('El area es: {}'.format(area))
    print('El volumen es: {}'.format(volumen))

# c) funciona con parametros y que retorna area y volumen
def cilindro_c(r, h):
    area = pi * (r ** 2) * h
    volumen = 2 * pi * r * (r + h)
    
    return area, volumen


#a
# cilindro_a()

#b
# r = int(input('Ingrese el radio: '))
# h = int(input('Ingrese la altura: '))
# cilindro_b(r, h)

#c
r = int(input('Ingrese el radio: '))
h = int(input('Ingrese la altura: '))
area, volumen = cilindro_c(r, h)
print('El area es: {}'.format(area))
print('El volumen es: {}'.format(volumen))

