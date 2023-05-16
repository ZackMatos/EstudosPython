def primo(x):
    y = 1
    count = 1
    if x == 1:
       return "Não é primo"
    while x != y:
        y +=1
        if x % y == 0:
           count +=1
    if y == x and count == 2:
        return "É primo"
    else:
        return "Não é primo"

n = 1
print("Para parar digite zero ou um número negativo")
while n > 0:
    n = int(input("Digite um número inteiro:"))
    p = 1
    while p == 1:
     print(primo(n))
     p +=1
if n <= 0:
    quit()

       
