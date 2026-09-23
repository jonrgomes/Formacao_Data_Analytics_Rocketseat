# Criando um dicionário aninhado:
clientes = {
    "cliente1":{
        "nome": "Ana Paula",
        "idade": 23,
        "email": "ana@gmail.com",
        "cidade": "São Paulo"    
    },   
    "cliente2": {
        "nome": "Roberto Lima",
        "idade": 45,
        "email": "roberto@gmail.com",
        "cidade": "Rio de Janeiro" 
    },
    "cliente3": {
    "nome": "Mariana Lemos",
    "idade": 67,
    "email": "lemos@gmail.com",
    "cidade": "Curitiba"       
}
}
print(clientes)

# Acessando os dados do dicionário aninhado:
print(clientes["cliente1"])
print(clientes["cliente1"]["email"]) # Acessando apenas e-mail no objeto cliente1

# Percorrendo um dicionário aninhado:
for chave, valor in clientes.items():
    for chave_interna, valor_interno in valor.items():
        print(f"{chave_interna}: {valor_interno}")
    print()
    
# Adicionando um novo cliente ao dicionário aninhado:
clientes["cliente4"] = {
        "nome": "Pedro Messias",
        "idade": 87,
        "email": "pedro@gmail.com",
        "cidade": "Itajuipe" 
}

print(clientes["cliente4"])

# Atualizando dados de um cliente no dicionário aninhado:
clientes["cliente4"]["cidade"] = "Recife"

# Removendo um cliente do dicionário aninhado:
del clientes["cliente2"]

for chave, valor in clientes.items():
    for chave_interna, valor_interno in valor.items():
        print(f"{chave_interna}: {valor_interno}")
    print()
