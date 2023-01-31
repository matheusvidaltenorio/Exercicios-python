from math import hypot

cateto_oposto = float(input('Digite o valor do cateto Oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipo = hypot(cateto_adjacente, cateto_oposto)

print('A hipotenusa é {}'.format(hipo))