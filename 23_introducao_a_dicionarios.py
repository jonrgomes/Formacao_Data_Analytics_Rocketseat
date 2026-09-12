# Sintaxe básica:
carros = {}

# pessoas = {
#     "nome": "José da Silva",
#     "Idade": 23,
#     "Altura": 1.99,
#     "Peso": 65.4,
#     "Habilitado": True
# }

# for chave, valor in pessoas.items():
#     print(f"{chave}: {valor}")

# # Acessando um item de um dicionário:
# print(pessoas["nome"])
# print(pessoas["Idade"])

# # Não acieta valores duplicados:

# pessoas = {
#     "nome": "José da Silva",
#     "Idade": 23,
#     "Altura": 1.99,
#     "Peso": 65.4,
#     "Peso": 78.5, #repete sempre o último valor
# }
# for chave, valor in pessoas.items():
#     print(f"{chave}: {valor}")

# Modificando um item de um dicionário:
pessoas = {
    "nome": "José da Silva",
    "Idade": 23,
    "Altura": 1.99,
    "Peso": 65.4,
}

pessoas["Peso"] = "2.5"
for chave, valor in pessoas.items():
    print(f"{chave}, {valor}")


# Tamanho de um dicionário:
print(len(pessoas))