#! /usr/bin/python

# funciones auxiliares
def may(a, b):
    if a > b:
        return a
    else:
        return b

def min(a, b):
    if a < b:
        return a
    else:
        return b

def mayor(x, y, z):
    return may(may(x, y), z)

def menor (x, y, z):
    return min(min(x, y), z)

def ordenar(x, y, z):
    _may = mayor(x, y, z)
    _men = menor(x, y, z)
    medio = x + y + z - (_may + _men)

    return _men, medio, _may

num_may = mayor(3, 7, 11)
num_men = menor(3, 7, 11)
print(num_may)
print(num_men)
print(ordenar(11, 3, 7))
