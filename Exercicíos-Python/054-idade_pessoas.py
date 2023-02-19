import datetime
cmaior = 0
cmenor = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = datetime.datetime.today().year - ano
    if idade >= 21:
        cmaior+=1
    else:
        cmenor+=1
print('{} Atingiram a maioridade'.format(cmaior))
print('{} não atingiram a maioridade'.format(cmenor))