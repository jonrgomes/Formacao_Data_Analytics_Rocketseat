# Criando uma lista aninhada:

colaboradores = [
    ["Nome", "Cargo", "Departamento"],
    ["Alice", "Analista", "Financeiro"],
    ["Carlos", "Gerente", "Vendas"],
    ["Julia", "Estagiaria", "RH"],
]
print(colaboradores)


# Acessando um intem em listas aninhadas:
print(colaboradores[2][2])

# Modificando um elemento da lista aninhada:
colaboradores[1][1] = "Cordenador"
print(colaboradores[1])

# Percorrendo uma lista aninhada:
for lista in colaboradores:
    for dados in lista:
        print(dados, end=", ")
    print()