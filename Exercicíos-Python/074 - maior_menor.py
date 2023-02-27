import random

numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'O valores sorteados foram ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f' O menor valor sorteado foi {min(numeros)}')
