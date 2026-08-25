# Operador E (and):
idade =  20
tem_carteira = True
print(idade >=18 and tem_carteira)

# Operador OU (or):
tem_ingresso = False
nome_na_lista = True
print(tem_ingresso or nome_na_lista)
"""
True or Treue = True
Treu or False = True
False or False = False
False or True = True

"""
# Operador Não (not):
logado = True
print(not logado)

# Prioridade dos Operadores
"""
parentes ()
1 not 
2 and
3or

"""
# Verificando os precedentes
a = True 
b = False
c = True
resultado = not a or b and c
print(resultado)

# Exemplo
cidade =  'São Paulo'
idade = 34
print(cidade == 'São Paulo' or idade >= 18)