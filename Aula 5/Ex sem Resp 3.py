import os as console

Contador = 1 

Numeros = []
NumerosDobrados = []

while Contador <= 5:
    Numeros.append( int(input('Digite um Número: ')))
    Contador = Contador + 1 
    
console.system('clear')
    
for Lista in Numeros:
    print(Lista * Lista)