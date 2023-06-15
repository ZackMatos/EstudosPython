lista_alunos = []
while True:
    alunos = input("Informe o nome do aluno:")
    lista_alunos.append(alunos)
    continuar = input("Deseja continuar? S/N:")
    lista_alunos.sort()
    if continuar.upper() == "N":
        break
for alunos in lista_alunos:
    print(alunos)