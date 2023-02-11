from random import randint
import time
maquina = randint(1, 3)
Jogador = int(input("Digite um numero para cada opção e veja se você ganha da máquina:\n1 - TESOURA\n2 - PAPEL\n3 - PEDRA.\nDigite sua opção: "))
print("JO")
time.sleep(3)
print("KEN")
time.sleep(3)
print("PO!!!")

if maquina > Jogador:
    print("="*20+"\nA maquina ganhou!")
elif maquina < Jogador:
    print("A maquina perdeu, e você ganhou!")
else:
    print("EMPATE")