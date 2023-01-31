import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
list = [a, b, c, d]
aluno_escolhido = random.choice(list)
print('O aluno escolhi foi: {} '.format(aluno_escolhido))

