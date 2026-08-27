# # Craindo uma String no Python
nome = 'Jonatas'
nome2 = "Gomes"

texto = 'Estou aprendendo "Python"'
print(texto)

# Tamanho da string
print(len(nome))
print(len(nome2))

# Operdador in - verifica a existencia de um caractere e retorna um valor booleano
print('a' in nome)
print('y' in nome2)

# Operador not in - verifica a inexistencia de um caractere e retorna um valor booleano
print('t' not in nome)
print('d' not in nome2)

# Cadeia de caracteres - Strings são imultavei
texto ='Python'
print(texto[1])

# Metodo capitalize
nome = 'jose'
nome = nome.capitalize()
print(nome)

# Deixa em caixa alta
nome = 'mario'
print(nome.upper())

# Deixar em caixa baixa
nome = 'MARIO'
print(nome.lower())