import time

primeiro_termo = int(input('Digite o valor do termo: '))
razao = int(input('Digite o valor da Razão:  '))
pa = primeiro_termo
c = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(pa), end=' ')
        pa = pa + razao
        time.sleep(1)
        c += 1
    print('PAUSA')
    mais = (int(input('Para mais digite algum valor e parar digite 0:\n')))
print('Fim da P.A')
