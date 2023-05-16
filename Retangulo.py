largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
contador_l = 0
contador_a = 0
hashtag = "#"
while contador_a != altura:
    while contador_l != largura:
        if altura > 1 and largura > 2:
           print(hashtag, end = "")
        print(hashtag, end = "")
        contador_l+=1
    print()
    contador_a +=1
    
