numeros = []
while True:
    valores = int(input("Digite um número inteiro:"))
    numeros.append(valores)
    continuar = input("Deseja continuar? S/N:")
    if continuar.upper() == "N":
        break
apagar = input("Deseja apagar os números pares ou ímpares? P- PAR/ I - IMPAR:")
if apagar.upper() == "P":
    for pares in numeros:
        if pares % 2 == 0:
         numeros.remove(pares)
    print("Após excluir os pares sobraram os seguintes números ímpares: {}".format(numeros))
else:
     for impares in numeros:
         if impares % 2 != 0:
             numeros.remove(impares)
     print("Após excluir os ímpares sobraram os seguintes números pares: {}".format(numeros))
    
