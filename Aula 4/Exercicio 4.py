NumeroDigitado = 0 
TentativaAtual = 1 

while (NumeroDigitado != 8) and (TentativaAtual <= 3):
    NumeroDigitado = int(input('Digite um número de 1 á 10: '))
    TentativaAtual += 1 
    
    
    if NumeroDigitado == 8: 
        break
if NumeroDigitado == 8: 
    print('Parabéns você acertou, era 8.')
else:
    print('Que pena ! Era o 8.')