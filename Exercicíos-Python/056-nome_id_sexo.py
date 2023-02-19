idmaior = 0
idmenor = 0
sexof = ''
sexom = ''
nomemMAIOR = ''
nomemMENOR = ''
nomefMAIOR = ''
nomefMENOR = ''
mediaid = 0
cont = 0
for c in range(1, 5, 1):
    print('====== {} PESSOA ======'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade:  '))
    sexo = str(input('Digite o sexo: [M/F]: ')).upper().strip()
    mediaid += idade
    if c == 1:
        idmaior = idade
        idmenor = idade
        sexom = sexo
        sexof = sexo
        nomem = nome
        nomef = nome
    else:
        if sexo == 'f' or sexo == 'F':
            if idade < 20:
                cont += 1

            if idade > idmaior:
                idmaiorf = idade
                nomefMAIOR = nome
            if idade < idmenor:
                idmenorf = idade
                nomefMENOR = nome

        if sexo == 'm' or sexo == 'M':

            if idade > idmaior:
                idmaiorm = idade
                nomemMAIOR = nome
            if idade < idmenor:
                idmenorm = idade
                nomemMENOR = nome

print('Media de idades das 4 pessoas é {}'.format(mediaid/4))
print('O nome do homem mais velho é ', nomemMAIOR)
print('Existe {} mulheres menores que 20'.format(cont))
