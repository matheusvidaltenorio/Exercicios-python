import random
maquina = random.randint(0, 5)
usuario = int(input('Digite um valor: '))

if usuario == maquina:
    print('Parabéns, Você Acertou!')
else:
    print('Que desastre, você errou =(, tente novamente.')