# Instrução While True: 
"""
while True:
    Executa o bloco de código
    if condição: (Se a condição for verdadeira)
        Executa esse bloco (break)
"""

while True: 
    senha = input('Digite sua senha: ')
    if senha == 'python':
        print('Acesso liberado!')
        break 
    else:
        print('Senha inválida! Digite novamente:')

# Instruções while True - Leia números e imprima na tela até que seja digitado 0:
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 0:
        print('Programa encerrado!')
        break
    else:
        print('Número inválido!')

# Comando break:
i = 1

while i < 10:
    if i == 3:
        break
    i += 1

# Comando continue - Imprima de 1 a 20, com exeção do número 10
x = 0

while x < 20:
    x += 1
    if x == 10:
        continue
    else:
        print(x)
   