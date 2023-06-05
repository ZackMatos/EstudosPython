def metade(valor):
    return "A metade de R${} é R${}".format(valor,valor / 2)

def dobro(valor):
    return "O dobro de R${} é R${}".format(valor,valor*2)

def aumentar(porcentagem,valor):
    return "Aumentando {}% temos R${}".format(porcentagem,valor + (valor * (porcentagem / 100)))

def diminuir(porcentagem,valor):
    return "Diminuindo {}% temos R${}".format(porcentagem,valor - (valor * (porcentagem / 100)))

def exceptions_float(msg):
    while True:
        try:
            x = float(input(msg))
        except (ValueError,TypeError):
            print("Você não digitou um número, tente novamente...")
            continue
        else:
            return x

def exceptions_int(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError,TypeError):
            print("Você não digitou um número, tente novamente...")
            continue
        else:
            return x