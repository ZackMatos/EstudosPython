nome_completo = str(input("Digite seu nome completo:")).strip()
separa = nome_completo.split()
print("Seu nome em letras maiúsculas é:{}\nSeu nome em letras minúsculas é:{}\nSeu nome tem ao todo {} letras\nSeu primeiro nome é {} que tem {} letras".format(nome_completo.upper(),nome_completo.lower(),len(nome_completo) - nome_completo.count(' '),separa[0],nome_completo.find(' ')))