soma_produtos = cont1000 = 0
produto_barato = ' '
cont = 0

while True:
    nome_produto = str(input('Nome do Produto: '))
    preco_produto = float(input('Digite o valor do produto: '))
    soma_produtos += preco_produto
    if preco_produto > 1000:
        cont1000 += 1
    if cont == 0:
        menor = preco_produto
        produto_barato = nome_produto
    else:
        if preco_produto < menor:
            menor = preco_produto
            produto_barato = nome_produto
    cont += 1
    parada = int(input('Quer CONTINUAR? 1 - SIM e 2 - NÃO: '))
    if parada == 2:
        break
print(f'O total de produtos foi {soma_produtos}')
print(f'Produtos que foram mais de mil, foram apenas {cont1000}')
print(f'O nome do produto mais barato é {produto_barato}, que custa R${menor}')


