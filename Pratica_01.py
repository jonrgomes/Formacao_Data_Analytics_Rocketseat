# # 1 -variáveis tipos de Dados:
# nome = 'Angels'
# classe = 'Guerreiro'
# nivel = 5
vida = 100.0
# esta_vivo = True

# # 2 - Saída de Dados:
# print('===FICHA DO PERSONAGEM===')
# print(f'Nome: {nome}')
# print(f'Classe: {classe}')
# print(f'Nível: {nivel}')
# print(f'Vida: {vida}')
# print(type(nome))
# print(type(classe))
# print(type(nivel))
# print(type(vida))
# print(type(esta_vivo))

# 3 - Entrada de Dados:
nome = input('Digite o nome do personagem: ')
classe = input('Digite a classe do personagem: ')
nivel = int(input('Digite o nível do persobagem: '))

# 4 - Operadores Aritiméticos:
dano_base = float(input('Digite o dano: '))
multiplicador_de_arma = float(input('Digite o multiplicador de armar: '))
dano_total = dano_base * multiplicador_de_arma
vida_restante = vida - dano_total
pontos_de_armadura = vida_restante % 10
print(f'Dano causado: {dano_total}')
print(f'Vida restante: {vida_restante}')
print(f'Pontos de armadura restantes: {pontos_de_armadura}')

# 5 Operadores relacionais:
print(f"Sobreviveu? {vida_restante > 0}")
print(f"Morreu exatamente no limite? {vida_restante == 0}")
print(f"É considerado veterano? {nivel >= 5}")

# 6 Operadores logicos:
pode_evoluir = nivel >= 5 and vida_restante > 0
esta_em_perigo = vida_restante< 20 or esta_vivo == False
# Usando a lógica, se a vida for 0, se da fim a vida!
nao_morreu = not (vida_restante <= 0)
print(f'Pode evoluir: {pode_evoluir}, Está em perigo: {esta_em_perigo}, Não morreu: {nao_morreu}')

# 7 Operações de atributos:
vida_restante += 15
dano_total -= 5
nivel += 1
print('=== FICHA DO PERSONAGEM ===')
print(f'Nome: {nome}')
print(f'Classe: {classe}')
print(f'Nível: {nivel}')
print(f'Dano causado: {dano_total}')
print(f'Vida restante: {vida_restante}')

# 8 if e else:
if vida_restante <= 0:
    print(f'{nome} foi derrotado...')
elif vida_restante<= 20:
    print(f'{nome} sobreviveu, mas está em perigo!')
elif nivel >= 5:
    print(f'{nome}, o veterano, venceu com faciliade!')
else:
    print(f'{nome} venceu a batalha!')
    