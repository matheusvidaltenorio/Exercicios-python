n = int(input('Digite um numero: '))
anterior = 0
atual = 1
proximo = 1
c = 0
while c < n:
    print('{} '.format(atual), end=' ')
    proximo = atual + anterior

    anterior = atual

    atual = proximo

    c += 1





