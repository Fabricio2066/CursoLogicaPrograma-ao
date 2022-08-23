import os as console

Contador = 1
Aluno = input('Digite o Nome do aluno: ')
Notas = []

while Contador <= 4:
    Notas.append( float(input('Digite a notas: ')))
    Contador = Contador + 1 
    
Total = Notas[0] + Notas[1] + Notas[2] + Notas[3]

Media = Total/4

console.system('clear')

print(f'A media do Aluno {Aluno} é: ', Media)