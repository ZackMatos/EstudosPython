def excecoes_int(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError,TypeError):
            print("Entrada de dados inválida, tente novamente...")
            continue
        else:
            return x
