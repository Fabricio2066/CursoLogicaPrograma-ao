import os 

NumeroDigitado = 0 
TentativaAtual = 0 
Nome = ''

while NumeroDigitado <= 50:
    NumeroDigitado = int(input('Digite um número: '))
    TentativaAtual += 1 
    
print('')
    
while len(Nome) < 3:
    Nome =  input('Digite seu nome: ')
    
    
os.system('clear')

print(f'Sr(a) {Nome}, você digitou {TentativaAtual} vezes o número.')