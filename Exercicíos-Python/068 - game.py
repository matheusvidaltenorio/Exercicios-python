import random
cont = 0
while True:
        jogador = int(input('Diga um valor: '))
        opcao = ' '
        while opcao not in 'PI':
                opcao = str(input('PAR OU IMPAR? [P/I]: ')).upper()
        computador = random.randint(1, 100)
        total = jogador + computador
        cont+=1
        if total % 2 == 0 and opcao == 'P':
                print(f'Você escolheu {jogador} e o computador escolheu {computador}. O total deu {total} que é PAR')
        elif total % 2 != 0 and opcao == 'I':
                print(f'Você escolheu {jogador} e o computador escolheu {computador}. O total deu {total} que é IMPAR')
        else:
                print('O jogador perdeu')
                break




