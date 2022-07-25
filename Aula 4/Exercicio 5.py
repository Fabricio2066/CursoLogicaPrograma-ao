nomePessoa = ' '
idadePessoa = 0

while len( nomePessoa ) < 3:
    nomePessoa = input('Digite seu primeiro nome: ')
    
    
while (idadePessoa<18) or (idadePessoa>50): 
     idadePessoa = int(input('Digite sua idade: '))
     
     
print('Cadastro realizado com sucesso! ')