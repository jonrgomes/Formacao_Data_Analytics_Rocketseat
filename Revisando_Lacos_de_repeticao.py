#O que é um laço de Repetição?
"""
É um estrutura que repete um bloco de código várias vezes, sem você precisar copiar e colar.
Em python temos dois principios: for e While

"""

# While = repete enquanto uma condição for verdadeira: 

contador = 1
while contador <= 5:
    print (contador)
    contador += 1
# # # Isso imprimi de 1 a 5. A condição é checada antes da repetição.
for numero in range(1, 6):
    print(numero)

# # # Mesmo resultado. O range(1, 6) gera os números de 1 até 5 (o último número não entra).
# # for numero in range(1, 11):
# #     print(numero)

soma = 0
numero = 1

while numero != 0:
    numero = int(input('Digite um valor: (0 para parar): '))
    soma += numero
print('A soma total foi:', soma)

# # Outro programa:

qtd_alunos = int(input('Digite a quantidade de alunos: '))
soma_notas = 0

for aluno in range(qtd_alunos):
    nota = float(input('Qual a nota obtida: '))
    soma_notas += nota

media = soma_notas / qtd_alunos
print(f'A média da turma é {media}!')

# Usando if e for:


qtd_alunos = int(input('Quantos alunos na turma? '))
soma_notas = 0

for alunos in range(qtd_alunos):
    nota = float(input('Qual a nota do aluno? '))
    soma_notas += nota

    if nota >= 6:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')

media = soma_notas / qtd_alunos
print(f'A média da turma é {media}')
