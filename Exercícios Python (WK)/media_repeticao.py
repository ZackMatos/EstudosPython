n = int(input("Digite a quantidade de números para fazer a média:"))
contador = 0
soma_de_n = 0
while contador < n:
       numero = int(input("Digite o valor:"))
       contador += 1
       soma_de_n += numero
media = soma_de_n / n
print("A média de {} é {:.2f}".format(soma_de_n,media))