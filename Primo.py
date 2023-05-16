n = int(input("Digite um número inteiro:"))
div = 1
if n % 2 == 0:
   div +=1
if n % 3 == 0:
   div += 1
if n % 5 == 0:
   div += 1
if n % 7 == 0:
    div += 1
if div == 2:
   print("primo")
      
