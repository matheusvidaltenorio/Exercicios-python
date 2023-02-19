n = 1
contpar = 0
contimpar = 0
while n != 0:
    n = int(input('Digite um número:  '))
    if n != 0:
        if n % 2 == 0:
             contpar = contpar + 1
        if n % 2 != 0:
             contimpar = contimpar + 1
print('Você digitou {} números pares e {} números ímpares.'.format(contpar, contimpar))