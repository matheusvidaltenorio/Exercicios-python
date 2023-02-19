import time

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = 0
maior = 0
while menu != 5:

    print('--------------------------------')
    menu = int(input('[1] PARA SOMAR\n[2] PARA MULTIPLICAR\n[3] PARA O VALOR MAIOR\n[4] PARA NOVOS NÚMEROS\n[5] PARA SAIR DO PROGRAMA\n>>Digite sua opção<<:'))
    print('--------------------------------')
    if menu == 1:
            soma = n1+n2
            print('Calculando...')
            time.sleep(3)
            print('====================\nA soma dos dois valores deram {}\n===================='.format(soma))
    elif menu == 2:
                multi = n1*n2
                print('Calculando...')
                time.sleep(3)
                print('====================\nA multiplicação dos dois valores deram {}\n===================='.format(multi))
    elif menu == 3:
            if n1 > n2:
                maior = n1
                print('Calculando...')
                time.sleep(3)
                print('O maior valor foi {}'.format(n1))
            elif n2 > n1:
                maior = n2
                print('Calculando...')
                time.sleep(3)
                print('O maior valor foi {}'.format(n2))
            else:
                print('Ambos números são iguais.')
    elif menu == 4:
            print('Digite novos números:')
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('\nEncerrando programa...')
    else:
        print('Erro de leitura de Código, Digite novamente.')

time.sleep(3)
print('O programa foi encerrado.')