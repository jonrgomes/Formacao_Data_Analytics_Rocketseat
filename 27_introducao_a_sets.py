# Sintxe de um set:
frutas = {"banara", "uva", "laranja"}
print(frutas)
print(type(frutas))

# Criar um set vazio:
frutas1 = set()
print(type(frutas1))

# Não é possível utilizar valores duplicados em sets:
numeros = {1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8}
frutas = {"banana", "uva", "banana", "maçã"}

print(numeros)
print(frutas)

# Tamanhpo de um set: 
print(len(frutas))

# Acessando um item de um set:
for x in frutas:
    print(x)
for y in numeros:
    print(y)
    
# Verificando se existe um item dentro de set:
if "banana" in frutas:
    print("Existe banana em frutas!")
else: 
    print("Não existe banana em frutas!")