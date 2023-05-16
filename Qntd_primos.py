def n_primos(n):
 if n < 2:
   return "Digite um número maior do que 2"
 contador = 1
 p = 1
 primo = 0
 while p != n:
      p += 1
      if n % p == 0:
       contador +=1
      if contador == 2 and p == n:
         n -= 1
         p = 1
         primo +=1
         contador = 1
      if contador > 2 and p == n:
         n -= 1
         p = 1
         contador = 1
      if n == 1 and p == n:
         return primo
