print("_____CADASTRO DE USUÁRIO______")

crie_usuario = input("Crie seu nome de usuário: ")

while True: # cria um loop infinito, pois não sabemos a quantidade de erro que o usuário pode ter:
    crie_senha = str(input("Crie seu senha: "))
    conf_senha = str(input("Confirme sua senha: "))
    
    if crie_senha == conf_senha: # comparação das senhas: 
        print("Cadastro realizado com susseço!")
        break # da um stop no laço se o confirmada as senhas!
    else: 
        print("As senha digitadas não conferem, favor digite novamente: ")
        
        
print("_______TELA DE LOGIN_______")

while True:
    login_usuario = str(input("Usuário: "))
    login_senha = str(input("Senha: "))
    
    if login_usuario == crie_usuario and login_senha == crie_senha:
        print("Acesso libera!")
        break
    
    else: 
        print("Usuário ou senha inválido, favor tente novamente!")
    
    

