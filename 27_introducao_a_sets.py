# # Sintaxe de um set:
frutas = {"banara", "uva", "laranja"}
print(frutas)
print(type(frutas))

#  Criar um set vazio:
frutas1 = set()
print(type(frutas1))

# Não é possível utilizar valores duplicados em sets:
numeros = {1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8}
frutas = {"banana", "uva", "banana", "maçã"}

print(numeros)
print(frutas)

# Tamanhpo de um set: 
print(len(frutas))

# # Acessando um item de um set:
for x in frutas:
    print(x)
for y in numeros:
    print(y)
    
# Verificando se existe um item dentro de set:
if "banana" in frutas:
    print("Existe banana no frutas!")
else: 
    print("Não existe banana no set frutas!")
    
# Não é possível editar um elemento, mas é possível adicionar novos elementos: 
frutas.add("pera")
print(frutas)
""" A função update adciona um elemento, mas ela itera sobre o que for adicionado: """

# # Concatenar os sets:
frutas1 = {"banana", "laranja"}
frutas2 = {"morango", "Kiwi"}

frutas1.update(frutas2)
print(frutas1)

# # Excluindo um valor de um set:
frutas1.remove("laranja")
print(frutas1)

frutas1.discard("Kiwi")
print(frutas1)

# Verificando se duas listas são iguais:
frutas1 = ["banana", "morango", "kiwi"]
frutas2 = ["morango", "morango", "banana", "morango", "kiwi", "kiwi", "banana", "morango"]
if set(frutas1) == set(frutas2):
    print("As frutas são iguais!")
else:
    print("As frutas são diferentes!")
    
# Método clear:
frutas1.clear()
print(frutas1)