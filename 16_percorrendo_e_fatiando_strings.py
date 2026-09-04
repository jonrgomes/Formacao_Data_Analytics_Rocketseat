# Percorrendo uma string com for
frase = "Jonatas será um DEV"

for a in frase:
    print(a)


print("_" * 50)
# Perconrrendo strings com while

amor = "Te amo Juliana!"
e = 0

while e < len(amor):
    print(amor[e])
    e += 1

print("_" * 50)

# Fatiamento de Strins
texto = "Flamengo é bom!!!"
"""
texto[inicio: fim - 1: passo]

"""
print(texto[0])
print(texto[-1])
print(texto[2: 10: 1])