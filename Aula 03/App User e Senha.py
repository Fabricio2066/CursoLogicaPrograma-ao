user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')


if user == "adm":
    if senha == "123":
        print('Acesso!')
    else:
        print('Senha errada!')
else:
    print('usuário incorreta, acesso negado!')