"""
from math import factorial
resp = 'S'
while resp == 'S':
    n = int(input('Digite um número: '))
    print('O fatorial de !{} é {}'.format(n, factorial(n)))
    resp = str(input('Digite se quer continuar? [S/N]: ')).upper()
print('O programa fechou.')
"""
n = int(input('Digite um valor para o fatoriaL: '))
c = n
f = 1
print('Calculando Fatorial de {}! = '.format(n), end='')
while c > 0:
     print(' {} '.format(c), end='')
     print(' x ' if c > 1 else ' = ', end='')
     f *= c
     c -= 1
print(' {} '.format(f))
