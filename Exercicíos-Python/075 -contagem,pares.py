valores = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os valores {valores}')

print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu {valores.index(3) + 1} vezes.')
else:
    print('Não foi visto o 3 em nenhuma posição.')
print('Os valores pares foram: ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')

# achar somente os pares.
