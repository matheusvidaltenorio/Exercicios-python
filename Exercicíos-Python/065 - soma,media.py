n = int(input('Digite um valor: '))
cont = 0
soma = 0
maior = 0
menor = 0
media = 0
while n != 0:
    if n != 0:
        if cont == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        soma += n
        cont += 1
        media = soma / cont

    n = int(input('Digite um valor: '))


print('A média dos valores foi {:.2f}'.format(media))
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
