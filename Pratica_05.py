# # Exercício com dicionários:
# """
# venda individual com várias informações — tipo uma linha de planilha ()
# """
# venda = {"produto": "Caneta", "quantidade": 10, "preco_unitario": 2.5}

# print(venda["quantidade"])
# print(venda["preco_unitario"])

# venda_total = venda["quantidade"] * venda["preco_unitario"]
# print(f"A venda total é de {venda_total:.2f}R$!".replace(".", ","))

# # Cadastro de Produtos em sistema: 

# produtos = []

# while True:
#     nome = input("Nome do produto: ")
#     preco_produto = float(input("Preço do produto: "))
    
#     novo_cadastro = input("Deseja prosseguir (S/N): ")
    
#     if novo_cadastro.lower() == "n":
#         break
    
    
# # Barbearia, marcando horário: 

# barber_cliente = []

# while True:
#     nome_cliente = input("Nome do cliente: ")
#     horario_marcado = str(input("Horário marcado: "))
    
#     dados_agenda = {"nome": nome_cliente, "horario": horario_marcado}
#     barber_cliente.append(dados_agenda)
    
#     novo_horario = input("Temos uma nova agenda? (Y/N): ")
    
#     if novo_horario.lower() == "n":
#         break 

# for agenda in barber_cliente:
#     print(agenda)

# # Controle de estoque de Lojinha:

# produtos = []

# while True:
#     nome_produto = input("Nome do produto: ")
#     preco_produto = float(input("Preço: "))
#     quantidade_produto = int(input("Quantidade: "))
    
#     listagem = {"nome": nome_produto, "preco": preco_produto, "quantidade": quantidade_produto}
#     produtos.append(listagem)
    
#     novo_cad_produtos = input("Deseja cadastrar outro produto? (S/N): ")
    
#     if novo_cad_produtos.lower() == "n":
#         break 

# for estoque in produtos:
#     print(estoque)

# Controle de notas de alunos:

print("______CONTROLE DE NOTAS DOS ALUNOS_______")

alunos = []
while True:
    nome_aluno = input("Nome do aluno: ")
    nota_aluno = float(input("Nota: "))

    if nota_aluno >= 7:
        situacao = "Aluno aprovado"   
    else:
        situacao = "Aluno reprovado"
        
    turma = {"nome": nome_aluno, "nota": nota_aluno, "situação": situacao}
    alunos.append(turma)
    novo_aluno = input("Deseja lançar outa nota de aluno: (S/N)")
    
    if novo_aluno.lower() == "n":
        break
    
print("______Resumo da turma:___________")

total_alunos = len(alunos)
soma_notas = 0
aprovados = 0
reprovados = 0

for turma_A in alunos:
    print(turma_A)
    soma_notas += turma_A["nota"]
    
    if turma_A["situação"] == "Aluno aprovado":
        aprovados += 1 
    else:
        reprovados += 1

print("____CALCULANDO A MÉDIA DA TURMA_____") 

media_turma = soma_notas / total_alunos
print(f"total de alunos cadastrados: {total_alunos}")
print(f"Média geral da turma: {media_turma:.2f}")
print(f"Total de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")
       

    






