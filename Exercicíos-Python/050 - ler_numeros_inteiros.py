soma = 0 #acumulador
cont = 0 #CONTADOR
for c in range(1, 7, 1):
    valor = int(input('Digite O {} valor:  '.format(c)))
    if valor % 2 == 0:
        soma += valor
        cont+=1
print('Você informou {} numeros pares, e a soma foi {}'.format(cont, soma))

