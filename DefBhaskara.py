import math
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

def delta(a,b,c):
    return (b**2)-(4*a*c)

def raiz1 (a,b,c):
    return (-b+ math.sqrt(delta(a,b,c))) / ((2*a))

def raiz2 (a,b,c):
    return (-b - math.sqrt(delta(a,b,c))) / ((2*a))

valorDelta = delta(a,b,c)
if valorDelta < 0:
    print("Esta equação não possui resultados reais")
else:
        raiz_primeira = raiz1(a,b,c)
        raiz_segunda = raiz2(a,b,c)
        if raiz_primeira > raiz_segunda:
            print("Raiz1:",raiz_segunda,"Raiz2:",raiz_primeira)
        if raiz_segunda > raiz_primeira:
            print("Raiz1:", raiz_primeira,"Raiz2:",raiz_segunda)
        if valorDelta == 0:
            print("Esta esquação possui apenas um resultado real:",raiz_primeira)

       
            


