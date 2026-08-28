# Contar quantidade de vezes que um caracter aparece numa string
email = "jonrgomes@gmail.com"
print(email.count("a"))

# Mostrar a posição de um caracter em uma string
print(email.find(".com"))
print(email.find("@gmail.com"))

# Verifica se uma string começa com um caractere ou sequencia de caracteres especificos
print(email.startswith("jon"))

# Verifica se uma string começa com um caractere ou sequencia de caracteres especificos
print(email.endswith(".com"))

# verificar se uma uma string possui valor numérico
cpf = "05079113389"
print(type(cpf))
print(cpf.isnumeric())

# Verificar se apenas são letras
print(cpf.isalpha())

# Verificar se o conteudo da stringa são letras e numeros
animal = "cachorro"
print(animal.isalnum())

# Remover espaços
