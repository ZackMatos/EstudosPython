from operator import itemgetter
contatos =  {"@joãogomes": "João Gomes", 
            "@bruna_iconica": "Bruna Marquesine",
            "@carla": "Carla",
             "@rbiana": "Fabiana"
            }
# for insta, nomes in sorted(contatos.items()):
#     print("{} --> {}".format(insta,nomes))

# contatos = {"@joãogomes": 1.70,
#             "@bruna_iconica": 1.62,
#             "@carla": 1.67,
#             "@rbiana": 1.65}

# for insta,estatura in sorted(contatos.items(),key=itemgetter(1)):
#     print("{} --> {:.2f}m".format(insta,estatura))

# for insta,estatura in sorted(contatos.items(),key=itemgetter(1),reverse=True):
#     print("{} --> {:.2f}m".format(insta,estatura))

# backup = contatos.copy()
# print(backup)

# contatos.pop("@carla")
# print(contatos)

# contatos.popitem()
# print(contatos)

contatos.clear()
print(contatos)