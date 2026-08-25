# Sintaxe do comando for:
"""
for variavel in sequencia:
    Executa esse bloco de comandos
"""
# Exemplo de for com Str:
for x in 'Python para Dados':
    print(x)

# Exemplo de for com listas:
nomes = ['Jonatas', 'Vera', 'Joaquim', 'Vitor']
for i in nomes:
    print(i)

# For in range - Sintaxe: 
"""
for i in range(inicio, fim, passo)
1) for i in range(fim) = início = 0 e o passo = 1.
2) for i in range (início e fim) passo = 1
3) for i in range (início, fim, passo)
"""
for i in range (10):
    print(i)
for x in range (2, 21):
    print(x)
for z in range (2, 21, 2):
    print(z)
for d in range (-1, -10, -2):
    print(d)

# For com else
# Imprimir uma mensagem ao termino do loop

for i in range (1, 20):
    print(i)
else:
    print('Fim da execução do for!')
