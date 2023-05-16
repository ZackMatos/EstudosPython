totalSeg = input("Por favor, entre com o número de segundos que deseja converter:")
convert = (int(totalSeg))

a = convert // 86400
segRest = convert % 86400
b = segRest // 3600
segRest = convert % 3600
c = segRest // 60
segRest = convert % 60
d = segRest // 1

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
