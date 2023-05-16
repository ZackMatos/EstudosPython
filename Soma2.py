n = int(input("Digite um número inteiro:"))
count = 0
if n == 0:
   print(n)
if n > 0:
 while n!= 0:
   rest = n % 10 
   n = (n - rest) // 10 
   count = count + rest
   if n == 0:
    print(count)
    
