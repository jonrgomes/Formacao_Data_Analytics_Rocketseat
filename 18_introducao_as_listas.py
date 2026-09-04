# Criando listas
nome = []
nomes = ["João", "Maria", "André"]
numeros = [1, 2, 3, 4]
altura = [1.3, 1.4, 3.6]

# Acessando os itens de uma lista:
print(nomes[2])
print(altura[2])

# Verificando a existencia de um item na lista:
if "Mario" in nomes:
    print("O nome Joáo esta dentro da lista!")

else:
    print("Este nome não pertence a esta lista!")

# Modificando um valor de uma lista:
frutas = ["Laranja", "Maça", "Pera"]
frutas[2] = "Mamão"
print(frutas)