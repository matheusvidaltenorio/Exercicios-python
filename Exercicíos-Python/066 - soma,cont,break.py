soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram cotados {cont}')
print(f'A soma de todos números deu {soma}')