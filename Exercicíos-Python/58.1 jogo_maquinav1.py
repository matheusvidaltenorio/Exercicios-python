from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    acertou = jogador == computador
    if acertou:
        print('Valor correto! Acertou em {} tentativas'.format(palpites))
    else:
        if computador < jogador:
            print('Informe um valor menor.')
        else:
            print('Informe um valor maior.')