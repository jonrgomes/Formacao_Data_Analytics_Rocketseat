# Sintaxe do comando while
"""
while condição: (Enquanto a condição for verdadeira)
    Executar o bloco de comandos
"""

# Exemplo de utilização com contados 1 até 10:

i = 1

while i <= 10:
    print('Contagem:', i)
    i += 1

# Loop ifinito
"""
while i <= 10:
    print('Contagem:', i)

"""

# Validação de strings com while:
senha = input('Digite sua senha de acesso ao sistema: ')

while senha != 'python':
    senha = input('Senha errada, tente novamente:')

print('Senha correta! O acesso foi liberado!')

# # Usuário tem que digitar um valor entre 1 e 10:

numero = int(input('Digite um numero: '))

while numero > 10:
    numero = int(input('Número não aceito, favor digite outro número: '))

print('Parabéns, você acertou, retire seu prêmio no caixa 5!')