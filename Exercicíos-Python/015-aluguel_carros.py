dias = int(input('Quantidade de dias alugado: '))
rodagem = float(input('Quantos Km rodou:'))
vlr_dia = dias*60
vlr_km = rodagem*0.15
total = vlr_dia+vlr_km
print('O total a pagar é R${:.2f}'.format(total))