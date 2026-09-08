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
colaboradores[1][1] = "Cordenadora"
print(colaboradores[1])

# Percorrendo uma lista aninhada:
for lista in colaboradores:
    for dados in lista:
        print(dados, end=", ")
    print()

# Percorrendo uma lista aninhada.2:
for dados in colaboradores[1:]:
    nome, cargo, departamento = dados
    print(f"{nome} trabalha como {cargo} no departamento {departamento}")

# Exemplo com range:
for i in range(len(colaboradores)):
    for j in range(len(colaboradores[i])):
        print(colaboradores[i][j], end= ", ")
    print()