a = int(input('Digite um valor:  '))
b = int(input('Digite um valor:  '))
c = int(input('Digite um valor:  '))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O maior é o {}'.format(maior))
print('O menor é o {}'.format(menor))
