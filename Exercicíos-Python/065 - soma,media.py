cont = soma = maior = menor = media = 0
resp = 'S'
while resp == 's' or resp == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input('Quer continuar [S/N]')).upper().split()[0]
media = soma / cont
print('\nAcabou')
print('A média dos valores foi {}'.format(media))
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
