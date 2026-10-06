# Nível Iniciante: O Relatório de Vendas (Filtragem e Transformação)
vendas = [
    {"id": 1, "valor": "150.50", "status": "concluida"},
    {"id": 2, "valor": "89.90", "status": "cancelada"},
    {"id": 3, "valor": "210.00", "status": "concluida"},
    {"id": 4, "valor": "45.00", "status": "pendente"},
]

fat_total = 0
qtd = 0
for venda in vendas:
    if venda["status"] == "concluida":
        texto = venda["valor"]
        numero = float(texto)
        venda["valor"] = numero
        fat_total += venda["valor"]
        qtd += 1

ticket_medio = fat_total / qtd

print(f"Faturamento total: R${fat_total}")
print(f"Ticket médio: R${ticket_medio}")   
        
# Nível Intermediário: Logs de Utilizadores
# logs = [
#     {"user_id": 101, "pagina": "home", "tempo_segundos": 45},
#     {"user_id": 102, "pagina": "checkout", "tempo_segundos": 120},
#     {"user_id": 101, "pagina": "perfil", "tempo_segundos": 60},
#     {"user_id": 103, "pagina": "home", "tempo_segundos": 30},
#     {"user_id": 102, "pagina": "home", "tempo_segundos": 15},
# ]
# # Crie um novo dicionário (o seu "caderno de anotações") onde a chave seja o user_id e o valor seja o tempo total gasto por esse utilizador. (Exemplo do resultado esperado: {101: 105, 102: 135, ...}).
# tempo_por_usuario = {}
# for venda in logs:
#     usuario = venda["user_id"]
#     tempo = venda["tempo_segundos"]
#     if usuario not in tempo_por_usuario:
#         tempo_por_usuario[usuario] = 0
#     tempo_por_usuario[usuario] += tempo
    
# print(tempo_por_usuario)
