altura = float(input("Digite sua altura:"))
sexo = input("Digite seu sexo [M/F]:")
if sexo.upper() == "M":
    print("Seu peso ideal será de {:.2f}Kg".format((72.7*altura) - 58.0))
elif sexo.upper() == "F":
    print("Seu peso ideal será de {:.2f}Kg".format((62.1 * altura) - 44.7))
else:
    print("Opção inválida")