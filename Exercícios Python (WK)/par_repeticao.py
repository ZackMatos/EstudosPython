contador = 0
par = 0
while contador < 5:
      par_ou_impar = int(input("Digite um número:"))
      if par_ou_impar % 2 == 0:
         print("O número {} é PAR!!!".format(par_ou_impar))
         par += 1
      contador += 1
print("Desses 5 números {} são pares".format(par))
      