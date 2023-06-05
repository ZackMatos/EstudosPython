temperatura = float(input("Informe a temperatura em ºC: "))
converter = ((temperatura / 5) * 9) + 32
print("A temperatura de {}ºC corresponde a {:.1f}ºF!".format(temperatura,converter))