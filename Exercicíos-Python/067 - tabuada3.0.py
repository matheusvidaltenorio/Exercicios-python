while True:
    tabuada = int(input('Quer ver a tabuada de qual valor: '))
    if tabuada < 0:
        print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!')
        break
    for c in range(1, 11, 1):
        print(f'{tabuada} x {c} = {tabuada*c}')
