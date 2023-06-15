'''Os professores de Educação Física estão organizando uma seletiva para montar a equipe de natação. Para isso, eles convocaram os 7 melhores tempos da última competição e marcaram o tempo de cada um dos nadadores, na prova dos 25 metros, estilo nado livre.
Considerando que não houve tempos iguais, construa um programa que leia o nome e o tempo (em segundos) de cada atleta e, em seguida, gere o seguinte relatório: a) nadador com o melhor tempo;  b) nadador com o pior desempenho e; c) tempo médio dos nadadores'''

#Minha resolução
nadadores = []
tempo = []

while True:
    nome_nadador = input("Digite o nome do nadador: ")
    tempo_nadador = int(input("Digite o tempo do nadador em segundos: "))
    nadadores.append(nome_nadador)
    tempo.append(tempo_nadador)
    continuar = input("Ainda há nadadores que deseja incluir na lista? S/N:")
    if continuar.upper() == "N":
        break

melhor_tempo = tempo.index(min(tempo))
pior_desempenho = tempo.index(max(tempo))
media = sum(tempo) / len(tempo)

segundos_melhor_tempo = min(tempo)
segundos_pior_tempo = max(tempo)

print(nadadores)
print(tempo)

print("O nadador com o melhor tempo foi {} que concluiu a prova em {} segundos".format(nadadores[melhor_tempo],segundos_melhor_tempo))
print("O nadador com pior desempenho foi {} que concluiu a prova em {} segundos".format(nadadores[pior_desempenho],segundos_pior_tempo))
print("A média de tempo dos nadadores foi de {:.2f} segundos".format(media))
