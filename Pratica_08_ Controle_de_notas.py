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
       