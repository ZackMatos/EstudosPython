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

def test_primos1000():
    assert n_primos(1000) == 168
def test_primos1():
    assert n_primos(1) == "Digite um número maior do que 2"
def test_primos997():
    assert n_primos(997) == 168
def test_primos3():
    assert n_primos(3) == 2
def test_primos2():
    assert n_primos(2) == 1
def test_primos13():
    assert n_primos(13) == 6
def test_primos14():
    assert n_primos(14) == 6
def test_primos0():
    assert n_primos(0) == "Digite um número maior do que 2"
