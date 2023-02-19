import time

primeiro_termo = int(input('Digite um valor: '))
razao = int(input('Digite um valor:  '))
pa = primeiro_termo
c = 1
while c < 11:
    print('{} - '.format(pa), end=' ')
    pa = pa + razao
    time.sleep(1)
    c += 1
print('Fim da P.A')
