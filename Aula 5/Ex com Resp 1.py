import os as console 
Contador = 0 
QuantidadesNomes = int(input('Digite o número de nomes:'))
ListaNomes = []

while Contador  < QuantidadesNomes:
    ListaNomes.append( input('Digite o nome: '))
    Contador = Contador + 1
    
console.system("clear")
print('Os nomes são')
for Nomes in ListaNomes:
    print(Nomes)