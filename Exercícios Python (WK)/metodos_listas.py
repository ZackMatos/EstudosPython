idades = []
while True:
   pessoa = int(input("Digite a idade da pessoa: "))
   idades.append(pessoa)
   continuar = input("Deseja continuar? S/N:")
   if continuar.upper() == "N":
      break
print("O mais novo tem {} anos".format(min(idades)))
print("O mais velho tem {} anos".format(max(idades)))
print("A soma das idades é igual a {}".format(sum(idades)))
media = sum(idades) / len(idades)
print("A lista tem {} elementos".format(len(idades)))
print("A média das idades é de {:.2f} anos".format(media))