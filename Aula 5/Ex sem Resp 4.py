import os 

Contador = 1 
ListaDeNomes = []

while Contador <= 10:
    ListaDeNomes.append(input('Digite um nome: '))
    Contador = Contador + 1 

os.system('clear')

print('Crescente')
ListaDeNomes.sort()
print(ListaDeNomes)

print('Decrescente')
ListaDeNomes.sort(reverse=True)
print(ListaDeNomes)