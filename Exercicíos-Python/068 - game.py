import random

while True:
        jogador = int(input('Diga um valor: '))
        opcao = str(input('PAR OU IMPAR? [P/I]: ')).upper()
        computador = random.randint(1, 100)
        total = jogador + computador
        if opcao == 'p':
            par = total % 2 == 0



