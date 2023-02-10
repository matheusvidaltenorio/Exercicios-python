

num = float(input("Digite um valor: "))
escolha = int(input("ESCOLHA UMA DAS OPÇÕES ABAIXO PARA PODER REALIZAR A CONVERSÃO:\nDigite 1 para BINÁRIO\nDigite 2 "
                    "para OCTAL\nDigite 3 para hecxadecimal. Sua escolha foi:\n"))


if escolha == 1:
              print(f"O seu numero em Binário ficará assim {num:b}".format(num))
elif escolha == 2:

              print(f"O seu numero em Binário ficará assim {num}:o}".format(num))
elif escolha == 3:
              calc = num/16
              print(calc)