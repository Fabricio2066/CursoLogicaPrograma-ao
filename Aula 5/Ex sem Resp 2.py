Contador = 1 
QuantDeNumeros = int(input('Digite a qtd de Números: '))

ListaDeNumeros = []

while Contador <= QuantDeNumeros:
    ListaDeNumeros.append(int(input('Digite um número: ')))
    Contador = Contador + 1 
    
print('Crescente')
ListaDeNumeros.sort()
print(ListaDeNumeros)
print('Decrescente')
ListaDeNumeros.sort(reverse=True)
print(ListaDeNumeros)
