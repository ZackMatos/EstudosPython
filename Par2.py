n = int(input("Digite um número inteiro:"))
count = 0
count2 = 0
i = n
p = n
while i > 0:
      count+=1
      if count % 2 !=0:
          print("Ímpar",count)
          i -=1
while p > 0:
      count2 +=1
      if not count2 % 2 !=0:
          print("Par",count2)
          p-=1
