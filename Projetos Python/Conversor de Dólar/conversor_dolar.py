from exceptions import exceptions_float
quantia = exceptions_float("Qual a quantia que você quer converter? R$")
converter = 0.20 * quantia
print("Com {:.2f} você pode pegar:US${:.2f}".format(quantia,converter))