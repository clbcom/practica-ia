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

n = int(input('Numero: '))
for i in range(n + 1):
    fact = factorial(i)
    print('{:5} => {:10}'.format(i, fact))
