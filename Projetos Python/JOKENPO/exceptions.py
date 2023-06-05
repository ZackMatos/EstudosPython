def excecoes_int(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError):
            print("\nVocê não digitou um número inteiro, tente novamente...\n")
            continue
        else:
            return x