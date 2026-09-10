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

# Posso ter elementos iguais dentro de uma tupla:
frutas = ("Maçã", "Pera", "Uva", "Pessego", "Uva")
print(frutas)

# Tamanho de uma tupla:
print(len(frutas))

# Extrai dados de uma tupla em variaveis:
numeros_a = (10, 50, 14)
(n1, n2, n3) = numeros_a

print(f"{n1}, {n2}, {n3}")

numeros = (10, 30, 60, 67, 567, 45)
(n1, n2, *n3) = numeros # usamos * qunado não sabemos a quantidade de elementos detro da tupla

print(n1)
print(n2)
print(n3)

# Percorrendo um tupla:
nomes = ("Erick", "Angelo", "Marcio", "Elias")

for i in nomes:
    print(i)

# Junta tuplas:
nomes_2 = ("André", "Mateus")

nomes_3 = nomes + nomes_2
print(nomes_3)

# Utilizando count:
print(nomes_3.count("André"))

# Index:
print(nomes_3.index("Mateus"))