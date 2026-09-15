""""
Exercício 1 — Percorrendo uma lista
Você tem a lista frutas = ["maçã", "banana", "uva", "manga"]. Use um for para imprimir cada fruta precedida do número dela na lista (começando em 1). 
"""

# 1 Declarar uma variavel frutas e atribuir uma lista:
frutas = ["maça", "banana", "uva", "manga"]

# Percorrer a lista frutas para e para fruta escrever a fruta e sua posição.
posicao = 1
for fruta in frutas:
    print(posicao, fruta)
    posicao += 1

# usar enumerate() (mais "pythônico", combina índice + valor automaticamente)

# # Percorrer a lista frutas para e para fruta escrever a fruta e sua posição, usa o enumarate com o inicio em 1 para escrever a posição de cada fruta da lista.
for posicao, fruta in enumerate(frutas, start=1):  
    print(posicao, fruta)
    posicao += 1