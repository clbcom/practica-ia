#! /usr/bin/python

def factorial(n):
    if (n < 0):
        print('parametros fuera de rango')
        return
    elif (n == 1 or n == 0):
        return 1

    else: 
        f = 1
        while (n > 0):
            f *= n
            n -= 1
        return f

def coeficiente_binomial(n, r):
    if n < r:
        print('Operacioon sin sentido, r no puede ser mayor que n, intentalo nuevamentes')
        return None

    numerador = factorial(n)
    denominador = factorial(r) * factorial(n - r)
    cb = numerador / denominador
    return cb

def input_parametros():
    n = int(input('Ingresa n:'))
    r = int(input('Ingresa r:'))

    return n, r

n, r = input_parametros()
cb = coeficiente_binomial(n, r)
print('Coeficiente binomial: {}'.format(cb))
