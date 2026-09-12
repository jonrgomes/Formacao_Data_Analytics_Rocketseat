# Exercício com dicionários:
""" 
Objetivo: a partir de vendas = [120, 85, 200, 150, 90, 300, 175], calcular total, média, maior e menor valor.
"""

vendas = [120, 85, 200, 150, 90, 300, 175]

total = 0 # cria um "acumulador" — uma variável que vai guardar a soma conforme o loop avança. Ela começa em zero pois não existe soma;
for x in vendas: # percorre a lista item por item. A cada volta, x recebe um valor diferente;
    total += x # (também pode escrever total += x) 
print(f"O total em vendas é {total}R$.")

# Calculando a média:

media =  total / len(vendas) # (len) retorna quantos elementos tem a lista
print(f"A média em vendas é de {media:.2f}R$.")

# A maio e menor venda:
maior = max(vendas)
menor = min(vendas)
print(f"A maior venda nos últimos 7 dias foi {maior}R$, sendo a menor {menor}R$!")