# Sintaxe do comando:
"""
if condição: (Se a condição for verdadeira)
    Executa esse bloco de comandos
elif condição2: ( Se a condição 2 for verdadeira)
    Executa esse bloco de comandos
elif condição3: ( Se a condição for verdadeira)
    Executa esse bloco de comandos
else:
    Executa esse bloco de comandos
"""

# Exemplo com if-elif-else: 
idade = 25
if idade < 10:
    print('Você é uma Criança.')
elif idade < 18:
    print('Você é um adolecente.')
elif idade < 65:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')


# Exemplo usando operadores lógicos: 
idade = 17
tem_carteira = True

if idade >= 18 and tem_carteira:
    print('Você é habilitado e pode dirigir!')
elif idade >= 18 and not tem_carteira:
    print('Você nãp é habilitado, não pode dirigir.')
elif idade < 18: 
    print('Você ainda não pode ter acesso a habilitação e dirigir!')