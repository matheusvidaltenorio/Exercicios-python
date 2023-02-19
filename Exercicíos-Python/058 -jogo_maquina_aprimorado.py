import random
maquina = random.randint(1, 10)
cont = 0
jogador = 0
while(maquina != jogador):

    jogador = int(input('Digite um valor: '))
    cont = cont + 1

    if maquina > jogador:
        print('Você errou, tente um número maior')
    if maquina < jogador:
        print('Você errou, tente um número menor')



print('Você acertou, A maquina pensou {} e o jogador pensou {} e precisou de {} tentativas'.format(maquina, jogador, cont))
