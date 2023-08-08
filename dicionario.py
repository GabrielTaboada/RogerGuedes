tabela = {"alface": [0.45, 2010], "batata": 1.2, "tomate": 2.3, "feijao": 1.5}
print(tabela)
print(tabela["alface"])
del tabela["tomate"]
print (tabela)

print("manga" in tabela)
print("batata" in tabela)

print(tabela["alface"])
tabela["alface"][0] = 1
tabela["alface"][1] = 2029
print(tabela["alface"])

