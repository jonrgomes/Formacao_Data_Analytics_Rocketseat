# ___REVISANDO LISTAS_____
# Uma lista é uma coleção ordenada e mutável. Você a usa quando tem vários itens que precisam ser guardados juntos e acessados por uma posição (índice).

dados = ["Python", "estudos","resiliencia"] # criando uma lista
dados.append("mentoria") # Adicionado um item na lista
print(dados[0:3]) # Acessando itens de uma lista

# O que você não pode esquecer:
""""
Índice zero: O primeiro elemento é lista[0], não lista[1].
Flexibilidade: Listas em Python aceitam tipos misturados. Você pode ter [1, "Texto", True] na mesma lista, embora na prática seja melhor manter listas homogêneas para evitar confusão.
"""

# _____REVISANDO OBJETOS______
"""
Em Python, absolutamente tudo é um objeto (incluindo a lista que acabamos de ver). Mas o verdadeiro poder surge quando você cria os seus próprios objetos através de Classes.
Uma Classe é a planta baixa da casa. O Objeto é a casa construída.
Um objeto carrega duas coisas:
""" 
# A sintaxe: Use a palavra-chave class e o método especial __init__ para definir o estado inicial.


# Criando a classe: (O molde)
class Aluno: 
    def __init__(self, nome, nota):
        self.nome = nome # atributo
        self.nota = nota # atributo
        
    def foi_aprovado(self): # Metodo
        if self.nota >= 7.0:
            return f"{self.nome} passou direto."
        return f"{self.nome} está de recuperação."
    
# Instanciando Objetos (construindo as peças):
aluno1 = Aluno("Carlos", 8.5)
aluno2 = Aluno("Ana", 5.0)

print(aluno1.nome)
print(aluno2.foi_aprovado())


    