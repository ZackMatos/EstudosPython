largura_parede = float(input("Digite a largura da parede: "))
altura_parede = float(input("Digite a altura da parede: "))
print("\nSua parede tem uma dimensão de {}x{} e sua área é de {}m²".format(largura_parede,altura_parede,largura_parede*altura_parede))
print("Para pintar essa parede, você irá precisar de {}l de tinta".format((largura_parede*altura_parede)/2))