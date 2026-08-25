# # 1.4 - Comentário em Python:
# print('o Pyhton é uma linguagem de programação que serve para desenvolvimento em ADS!')
# """
# Nesta linha de código explicamos de forma resumida o que é o Python!

# """
print('Estudos de ADS e Python.')
print('_' * 50)

# # 1.5 Váriáveis e Tipos de Dados:
nome_do_pet = 'Zaia'
idade_do_pet = 10
kg_de_racao_consumida_mes = 12.4
e_macho = True
print(type(nome_do_pet))
print(type(idade_do_pet))
print(type(kg_de_racao_consumida_mes))
print(type(e_macho))
print('_' * 60)

# 1.6 Sáida de Dados:
nome = 'Jonatas'
idade = 33
cidade = 'Itabuna'
print(nome, idade, cidade, sep=',')
cidades = ['Santos', 'Acre', 'Belém', 'Itabuna']
print(*cidades, sep='|')
n = 5
s = n * 2
print(s)
print(f'O dobro de {n} é {s}!')
print('_' * 60)

# 1.7 Entrada de Dados