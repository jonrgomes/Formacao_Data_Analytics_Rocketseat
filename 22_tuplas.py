# Definição de tuplas - SINTAXE:
carro = ("Gol", "Voyage", "Fusca")
print(carro)

# Verificando o tipo de dados:
# print(type(carro))

# # Acessando um elemento de uma tupla:
print(carro[0])
print(carro[1])
print(carro[2])

# Alterando dados de uma tupa:
auxiliar = list(carro) # converte em lista com uma variavel de apoio
print(auxiliar)

auxiliar[1] = "Brasília" # consegue a alteração via listas
print(auxiliar)

carro = tuple(auxiliar) # converte a variavel de apoio na variavel inicial
print(carro)