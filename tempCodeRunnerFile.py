# Nível Iniciante: O Relatório de Vendas (Filtragem e Transformação)
# vendas = [
#     {"id": 1, "valor": "150.50", "status": "concluida"},
#     {"id": 2, "valor": "89.90", "status": "cancelada"},
#     {"id": 3, "valor": "210.00", "status": "concluida"},
#     {"id": 4, "valor": "45.00", "status": "pendente"},
# ]
# # 1. Filtre a lista para manter apenas as vendas com status "concluida"
# status = []
# for venda in vendas:
#     if venda["status"] == "concluida":
#         status.append(venda)
# print(status)

# # 2. Converta os valores (que estão como string) para numérico (float).
# valor = []
# for venda in status:
#     texto = venda["valor"]
#     numero = float(texto)
#     venda["valor"] = numero
#     valor.append(venda)
# print(valor)

# # 3. Calcule e imprima o faturamento total e o ticket médio (faturamento dividido pelo número de vendas válidas).
# fat_total = 0
# for venda in valor: 
#     fat_total += venda["valor"]
    
# ticket_medio = fat_total / len(valor)

# print(f"Faturamento total: R${fat_total}")
# print(f"Ticket médio: R${ticket_medio}")   