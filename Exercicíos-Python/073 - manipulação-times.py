times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia',
         'Botafogo', 'Corinthias', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
         'Palmeiras', 'Bragantino', 'Santo', 'São Paulo', 'Vasco da Gama')

print(f'os 5 primeiros colocados foram {times[:5]}')
print(f'OS 4 ULTIMOS COLOCADOS FORAM {times[-4:]}')
print(f'A lista dos 20 times em ordem alfabética é {sorted(times)}')
print(f'O santos está na {times.index("Santo") + 1} posição.')