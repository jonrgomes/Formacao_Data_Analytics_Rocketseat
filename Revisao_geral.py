# Nível Iniciante: O Relatório de Vendas (Filtragem e Transformação)
vendas = [
    {"id": 1, "valor": "150.50", "status": "concluida"},
    {"id": 2, "valor": "89.90", "status": "cancelada"},
    {"id": 3, "valor": "210.00", "status": "concluida"},
    {"id": 4, "valor": "45.00", "status": "pendente"},
]

status = []
for venda in vendas:
    if venda["status"] != "cancelada" not in status:
        status.append(venda)
print(status)
print()