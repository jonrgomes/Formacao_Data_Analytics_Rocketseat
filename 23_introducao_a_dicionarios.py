# Sintaxe básica: (Também conhecida com objeto ou Json em via de regra)
carros = {}
pessoas = [  # criando uma lista de objetos de pessoas
    { 
        "nome": "Andre",
        "Idade": 23,
        "Altura": 1.99,
        "Peso": 65.4,
        "Habilitado": True  
    },
    {
        "nome": "Pedro",
        "Idade": 67,
        "Altura": 1.65,
        "Peso": 50,
        "Habilitado": False   
    }
]

# print(pessoas)

pessoas.append(
    {
        "nome": "João",
        "Idade": 67,
        "Altura": 1.65,
        "Peso": 50,
        "Habilitado": False   
}
               )



for x in range(len(pessoas)):
    print(pessoas[x])
    
    





# pessoa = {
#     "nome": "José da Silva",
#     "Idade": 23,
#     "Altura": 1.99,
#     "Peso": 65.4,
#     "Habilitado": True
# }

# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")

# # Acessando um item de um dicionário:
# print(pessoa["nome"])
# print(pessoa["Idade"])

# # Não acieta valores duplicados:

# pessoa = {
#     "nome": "José da Silva",
#     "Idade": 23,
#     "Altura": 1.99,
#     "Peso": 65.4,
#     "Peso": 78.5, #repete sempre o último valor
# }
# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")

# # Modificando um item de um dicionário:
# pessoa = {
#     "nome": "José da Silva",
#     "Idade": 23,
#     "Altura": 1.99,
#     "Peso": 65.4,
# }

# pessoa["Peso"] = "2.5"
# for chave, valor in pessoa.items():
#     print(f"{chave}, {valor}")


# # Tamanho de um dicionário:
# print(len(pessoa))

