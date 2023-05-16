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
              
          

    
    
