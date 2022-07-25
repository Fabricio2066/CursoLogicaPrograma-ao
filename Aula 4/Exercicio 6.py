import os 
AplicativoAberto = True 

while  AplicativoAberto: 
    print('Escolha uma das opções abaixo digitando o número')
    Escolha = int(input('''
        1) Fazer login
        2) Criar uma conta
        3) Sair 
        ''')) 
        
    
    os.system('clear')
    
    if Escolha == 3:
        AplicativoAberto = False
        
        
print('Bye!')