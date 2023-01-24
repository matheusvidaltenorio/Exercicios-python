valor = int(input('Digite o valor em metros: '))
km = valor/1000
hec = valor/100 
dec = valor/10
deci = valor*10
cent = valor*100
mili = valor*1000
print('O valor base é {}.'.format(valor))
print('Transformando em Km fica {} e em decametros fica {}.'.format(km, hec))
print('Transformando em Hectometros fica {} e em decimetros fica {}.'.format(dec, deci))
print('Transformando em Centimetros fica {:.0f} e em milimetros fica {:.0f}.'.format(cent, mili))