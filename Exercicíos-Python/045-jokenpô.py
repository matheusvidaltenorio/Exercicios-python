from random import randint
maquina = randint(1, 3)
Jogador = int(input("Digite um numero para cada opção e veja se você ganha da máquina:\n1 - TESOURA\n2 - PAPEL\n3 - PEDRA.\nDigite sua opção: "))

if maquina > Jogador:
    print("A maquina ganhou!")
elif maquina < Jogador:
    print("A maquina perdeu")
else:
    print("EMPATE")