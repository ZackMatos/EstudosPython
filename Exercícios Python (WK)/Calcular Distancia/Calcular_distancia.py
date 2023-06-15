from func_distancia import calcular_distancia
xa = float(input("Digite uma coordenada para X do ponto A:"))
ya= float(input("Digite uma coordenada para Y do ponto A:"))
xb= float(input("Digite uma coordenada para X do ponto B:"))
yb= float(input("Digite uma coordenada para Y do ponto B:"))
print("A distância entre esses dois pontos é: {:.2f}".format(calcular_distancia(xa,xb,ya,yb)))