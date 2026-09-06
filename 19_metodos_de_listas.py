# Tamanho de uma listas:
cores = ["Preto", "Azul", "Vermelho"]
print(len(cores))

# Inserindo dados em um lista (append):
print(cores[2])
cores.append("Liláz")
print(cores)

# Inserindo dados em uma posiçao especifíca: (insert):
frutas = ["Goiaba", "Laranja", "Abacates"]
frutas.insert(0, "Pera")
print(frutas)



# Juntando listas com extend:
nome_1 = ["Ana", "Paulo", "André"]
nome_2 = ["Pedro", "Alex", "Antonio"]

nome_1.extend(nome_2)
print(nome_1)

# # Removendo dados de uma lista (remove):
frutas = ["Laranja", "Amora", "Goiaba"]
frutas.remove("Amora")

print(frutas)

# Removendo dados de uma lista (pop), esse é utilizado para remover o último elemento ou escolhe o índice escolhido.

dados_1 = ["Blusa", "Camisa", "Calça"]
dados_1.pop()
dados_1.pop(1)
print(dados_1)
print(dados_1)

# Removendo dados de uma lista (del):
frutas = ["Laranja", "Amora", "Goiaba"]
del frutas[0]
print(frutas)

# Limpando a lista do programa (del):
frutas.clear()
print(frutas)