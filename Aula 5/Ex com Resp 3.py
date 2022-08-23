Contador = 1 
Numeros = []
while Contador <= 5:
    Numeros.append( int(input('Digite um valor: ')))
    Contador = Contador + 1 
    
print('Crescente')
Numeros.sort()
print(Numeros)

print('Decrescente')
Numeros.sort(reverse=True)
print(Numeros)