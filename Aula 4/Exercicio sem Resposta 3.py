import os as cmd
App_Aberto = True
Usuario = ""
Senha = ""
Saldo = 500 

while App_Aberto:
    escolha = input("""
    1) Fazer login
    2) Criar conta 
    3) Consultar Saldo
    4) Depositar
    5) Comprar 
    6) Sair
    
    Digite um número para selecionar, e aperte Enter
    =>""")
    
    cmd.system('clear')
    
    if escolha == '1':
        print('Você escolheu logar.')
        input('Aperte qualquer tecla para continuar...')
        cmd.system('clear')
    elif escolha == '2':
        print('Você escolheu se cadastrar.')
        input('Aperte qualquer tecla para continuar...')
        cmd.system('clear')
    elif escolha == '3':
        print(f'Você escolheu se consultar seu saldo. Ele é de R${Saldo}')
        input('Aperte qualquer tecla para continuar...')
        cmd.system('clear')
    elif escolha == '4':
        deposito = float(input('Digite o valor a depositar: '))
        Saldo += deposito
        input('Deposito realizado com sucesso!\n Aperte qualquer tecla para continuar...')
        cmd.system('clear')  
    elif escolha == '5':
        print('Você escolheu comprar.')
        input('Aperte qualquer tecla para continuar...')
        cmd.system('clear')    
    elif escolha == '6':
        print('Você escolheu sair.')
        input('Aperte qualquer tecla para continuar...')
        cmd.system('clear')      
        App_Aberto = False 
    else:
        print("Você escolheu uma opção invalida!")
        input('Aperte qualquer tecla para continuar...')
        cmd.system('clear')
        
        
        
        
        
        
        
        
        
        