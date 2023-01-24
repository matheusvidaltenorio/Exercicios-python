valor = int(input('Digite um valor: '))
desconto = valor*(5/100)
total = valor-desconto
print('O preço antigo é {}, e o novo preço é {:.2f}'.format(valor, total))
