# # Acessando valores de um dicionário com (índice e get):
pessoas = {
    "nome": "Jonatas Gomes",
    "idade": 33,
    "altura": 1.70,
    "habilitado": True
}

print(pessoas["nome"])
print(pessoas.get("habilitado"))

# retornando todo os dados de um dicionário:
print(pessoas.keys())

# retonando os valores de um dicionário:
print(pessoas.values())

# Retornando as chaves e valores de um dicionário:
print(pessoas.items())
for chave, valor in pessoas.items(): # percorrendo com for
    print(f"{chave}: {valor}")

# verificando se existe uma chave em um dicionário:
"nome" in pessoas # se existe
"nome" not in pessoas # se náo existe

# Alterando valores de um dicionário:
pessoas["idade"] = 40
print(pessoas)

pessoas.update({"altura":1.88})
print(pessoas)

pessoas.update({"idade":56, "altura":1.90, "habilitado":False})
print(pessoas)

# Adicionando um novo chave:valor no dicionário:
pessoas["CPF"] = "000.000.000-00"
pessoas.update({"RG":"000.000.00"})
print(pessoas)