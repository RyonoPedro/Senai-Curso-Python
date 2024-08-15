#usando operadores lógicos para simular a validação de senha

user_adm = 'admin'
senha_adm = 'admin'
senha_user = '4421'

    
while True:
    user = input('Digite o nome do usuário: ')
    senha = input('Digite a senha do usuário: ')
    if user == user_adm and senha == senha_adm:
        print('Acesso liberado para usuário administrador.')
        break
    elif not(user == user_adm) and senha == senha_user:
        print(f'Acesso liberado para usuário {user}')
        break
    elif senha_user and senha_adm != senha:
        print('Senha inválida, tente novamente')

