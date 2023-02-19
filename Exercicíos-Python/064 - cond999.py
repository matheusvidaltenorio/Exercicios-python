soma = 0
n = 0
cont = 0
while n != 999:
        n = int(input('Digite um valor: '))
        if n != 999:
             cont += 1
             soma += n
print('Foram digitados {} numeros e a soma deu {}'.format(cont, soma))

