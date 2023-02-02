distancia = float(input('Digite a distânica percorrida: '))

if distancia <= 200:
    preco_a = distancia*0.5
    print('O valor da passagem ficará de R${:.2f}'.format(preco_a))
else:
    preco_b = distancia*0.45
    print('O valor da passagem ficará de R${:.2f}'.format(preco_b))