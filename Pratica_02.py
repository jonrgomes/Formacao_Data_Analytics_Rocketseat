# 1 - Variáveis e Tipos de Dados:
produto = 'Geladeira'
categoria = 'Eletrodoméstico'
quantidade = 100
preco_unitario = 2400.99
em_estoque = True

# 2 Saída de Dados: 

print('=== Registro de Venda ===')
print(f'Produto: {produto}')
print(f'Categoria: {categoria}')
print(f'Quantidade: {quantidade}')
print(f'Preço unitário: R${preco_unitario}')
print('-----------------------------------------------')

# 3 Entrada de Dados: 

categoria = input('Qual a categoria desejada: ')
produto = input('Qual produto deseja: ')
quantidade = int(input('Qual quantidade deseja:'))
preco_unitario = float(input('Quanto deseja pagar em cada unidade: '))
desconto_percentual = 0
em_estoque = 0
print('---------------------------------------------------')

# 4 Operadores Aritiméticos: 
valor_total_da_venda = quantidade * preco_unitario
valor_desconto = valor_total_da_venda * 0.1
valor_final = float(valor_total_da_venda - valor_desconto)
print(f'O valor total da venda é R${valor_total_da_venda}!')
print(f'O desconto concedido é de R${valor_desconto}!')
print(f'Sua compra fica no valor de R${valor_final:.2f}!')
print('---------------------------------------------------')

# 5 Operadores Relacionais:

precificacao = valor_final > 1000
print(f"É uma venda de alto valor? {precificacao}")
variedade = quantidade == 0
print(f'A venda esta vazia? {variedade}')
preco_desconto = desconto_percentual >= 50
print(f'O desconto é considerado agressivo. {preco_desconto}')
print('---------------------------------------------------')

# Operadores Lógicos:

venda_valida = quantidade > 0 and preco_unitario > 0
precisa_revisao = desconto_percentual >= 50 or valor_final > 5000
fora_de_estoque = not em_estoque
