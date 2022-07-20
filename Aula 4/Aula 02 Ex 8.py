import os 

multa = float( input('Digite o valor: R$'))
diasAtraso = int(input('Digite o valor de dias atrasados: '))

print(f'O valor da multa é de R${( multa * ( 1 + 0.03 * diasAtraso) ) * 1.1}')