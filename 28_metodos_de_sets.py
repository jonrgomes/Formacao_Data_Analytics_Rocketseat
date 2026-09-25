# Criando um conjunto de numeros: 

a = {1, 2, 3}
b = {3, 4, 5}
c = {7, 8, 9}
d = {1, 2, 5, 8, 9}

# Metodo copy:
aux = a.copy()
print(aux)

# Metodos união (Juntar os elementos dos conjuntos):
a = {1, 2, 3}
b = {3, 4, 5}

aux = a.union(b) # primeira forma
print(aux)

aux = a | b # segunda forma
print(aux)

# Interseção (Apenas os elementos comuns entre os dois):
a = {1, 2, 3}
d = {1, 2, 5, 8, 9}

aux = a.intersection(d) # primeira forma
print(aux)

aux = a & d
print(aux)

# Diferença (Apenas o que não existe entre os conjuntos):
c = {7, 8, 9}
d = {1, 2, 5, 8, 9}

aux = c.difference(d) # primeira forma
print(aux)

aux = c - d
print(aux)

# Difença simetrica (retira o que aparece em comum em ambos os conjuntos):

a = {1, 2, 3}
b = {3, 4, 5}

aux = a.symmetric_difference(b)
print(aux)