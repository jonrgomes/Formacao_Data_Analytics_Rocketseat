# Percorrendo uma lista com for:
frutas = ["maçã", "laranja", "pera"]

for i in frutas:
    print(i)

# Percorrendo uma lista com range:
nomes = ["Antoni", "Marcos", "Pedro", "Eduardo"]

for e in range(len(nomes)):
    print(nomes[e])

# Percorrendo a lisa com while:
contador = 0
while contador < len(nomes):
    print(nomes[contador])
    contador += 1

# Fatiamento de listas:
nomes = ["Antoni", "Marcos", "Pedro", "Eduardo", "André"]
print(nomes[0:2:1])
print(nomes[2:5:2])