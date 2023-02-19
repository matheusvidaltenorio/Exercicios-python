import time

tabuada = int(input('Digite a tabuada que você deseja: '))
for c in range(1, 11, 1):
    print(tabuada, ' x ', c, ' = ', (tabuada*c))
    time.sleep(2)
