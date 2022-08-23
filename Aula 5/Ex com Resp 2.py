Contador = 1 


Numeros = []
NumeorsDobrados = []

while Contador <= 5:
    Numeros.append(int(input('Digite um valor: ')))
    Contador = Contador + 1 
    
for Valor in Numeros:
    NumeorsDobrados.append(Valor * 2)

print('Números Dobrados: ', NumeorsDobrados)