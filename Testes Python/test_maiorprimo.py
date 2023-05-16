def maior_primo(k):
    div = 1
    count = 2
    primo = 1
    if k == 1:
       return "Não há números primos"
    if k == 2:
        primo = k
        return primo
    while count != k:
          count +=1
          if k % count == 0:
              div +=1
              primo = k
          if div == 2 and count == k:
              éPrimo = True
              primo = k
              return primo
          if count == k and div != 2:
              k-=1
              count = 2
              div = 1
          if k == 3:
              primo = k
              return primo
            
#Testando a função maior_primo
def test_maiorprimo8():
    assert maior_primo(8) == 7
    
def test_maiorprimo2():
    assert maior_primo(2) == 2
    
def test_maiorprimo1000():
    assert maior_primo(1000) == 997
    
def test_maiorprimo10():
    assert maior_primo(10) == 7
    
def test_maiorprimo3():
    assert maior_primo(3) == 3
    
def test_maiorprimo14():
    assert maior_primo(14) == 13
    
def test_maiorprimo232():
    assert maior_primo(232) == 229
def test_maiorprimo1():
    assert maior_primo(1) == "Não há números primos"
