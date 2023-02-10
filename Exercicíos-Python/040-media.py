n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))
media = (n1+n2)/2
print("Tirando as notas {:.1f} e {:.1f}, a média do aluno será {:.2f}".format(n1, n2, media))

if media < 5:
    print("REPROVADO")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO.")
else:
    print("APROVADO")
