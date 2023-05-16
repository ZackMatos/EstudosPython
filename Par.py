n = int(input("Digite um número inteiro:"))
i = n
count = 0
if n == 0:
   print("Não há números pares")
while i > 0:
      count +=1
      if count % 2 == 0 and n !=0:
         print(count)
         i -= 1
      
