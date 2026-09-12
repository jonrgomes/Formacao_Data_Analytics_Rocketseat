# Exercício com dicionários:
"""
venda individual com várias informações — tipo uma linha de planilha ()
"""
venda = {"produto": "Caneta", "quantidade": 10, "preco_unitario": 2.5}

print(venda["quantidade"])
print(venda["preco_unitario"])

venda_total = venda["quantidade"] * venda["preco_unitario"]
print(f"A venda total é de {venda_total:.2f}R$!".replace(".", ","))

