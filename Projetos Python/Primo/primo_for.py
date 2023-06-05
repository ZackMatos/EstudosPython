from exceptions import exceptions_int
numero = exceptions_int("Digite um número: ")
div = 0
for x in range(1,numero + 1):
  if numero % x == 0:
    div+=1
if div == 2:
    print("É primo")
else:
    print("Não é primo")