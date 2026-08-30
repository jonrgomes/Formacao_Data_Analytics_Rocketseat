# Nome e descoberta de idade:

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
ano_atual = 2026
nova_idade = (2050 - ano_atual) + idade
print(f"Olá, {nome}, Você tem {idade} anos e em 2050 tera {nova_idade} anos!")

# Notas do Aluno
nota = float(input("Digite a sua nota:"))

if nota > 10 or nota < 0: 
    print("Nota inválida, difite uma nota entre 0 e 10!")
elif nota >= 9:
    print("Sua nota é Excelente!!")
elif nota >= 7:
    print("Sua nota é boa!")
elif nota >= 5:
    print("Sua nota é regular!")
else:
    print("Sua nota é insuficiente!")

# Laços de repetição
valor = int(input("Digite um número: "))
soma = 0

while valor != 0:
    print("Você digitou:", valor)
    soma += valor
    valor = int(input("Digite um número: "))
print(f"A soma é {soma}!")