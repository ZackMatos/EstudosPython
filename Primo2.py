n = int(input("Digite um número inteiro:"))
div = 1
prod = 1
while prod != n:
      prod += 1
      if n % prod == 0:
         div += 1

if div == 2 and prod == n:
   print("primo")
if prod == n and not div == 2:
   print("não primo")
      
