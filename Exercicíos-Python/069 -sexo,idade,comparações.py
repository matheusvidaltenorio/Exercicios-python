id18 = homem = mulher20 = 0
while True:
    idade = int(input('Digite sua idade:  '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [F/M]: ')).upper()
    if idade > 18:
        id18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    print('='*35)
    parada = int(input('Quer continuar? 1 - Sim e 2 - Não: '))
    print('=' * 35)
    if parada == 2:
        break

print(f'Existem {id18} pessoas com mais de 18')
print(f'Foram cadastrado(s) {homem} homens.')
print(f'As mulheres com menos de 20, tivemos {mulher20} cadastrada(s).')