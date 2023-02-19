cmaior = 0
cmenor = 0
for c in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        cmaior = peso
        cmenor = peso
    else:
        if peso > cmaior:
                    cmaior = peso
        if peso < cmenor:
                    cmenor = peso
print('O maior peso é o {}'.format(cmaior))
print('O menor peso é o {}'.format(cmenor))