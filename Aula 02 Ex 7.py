import os as Console 


    
print(25*'=')
print('# Cálculo do Triângulo #')
print(25*'=')
print('')

TrianguloA = input("Digite o Lado A do triângulo: ")
TrianguloB = input("Digite a Altura B do triângulo: ")

Console.system('clear')

input('Triangulo registrado! Pressione Enter para o próximo.')

Console.system('clear')









print(25*'=')
print('# Cálculo do Círculo #')
print(25*'=')
print('')

CirculoA = input("Digite o Raio do círculo: ")

Console.system('clear')

input('Círculo registrado! Pressione Enter para o próximo.')

Console.system('clear')










print(25*'=')
print('# Cálculo do Trapézio #')
print(25*'=')
print('')

TrapezioA = input("Digite o Comprimento A do trapézio: ")
TrapezioB = input("Digite o Comprimento B do trapézio: ")
TrapezioC = input("Digite a Altura B do trapézio: ")

Console.system('clear')

input('Trapézio registrado! Pressione Enter para o próximo.')

Console.system('clear')










print(25*'=')
print('# Cálculo do Quadrado #')
print(25*'=')
print('')

QuadradoA = input("Digite o Lado A do quadrado: ")

Console.system('clear')

input('Quadrado registrado! Pressione Enter para o próximo.')

Console.system('clear')









print(25*'=')
print('# Cálculo do Retângulo #')
print(25*'=')
print('')

RetanguloA = input("Digite o Comprimento A do retângulo: ")
RetanguloB = input("Digite o Comprimento B do retângulo: ")

Console.system('clear')

input('Retângulo registrado! Pressione Enter para o próximo.')

Console.system('clear')


print(25*'=')
print('# Relatorio Final #')
print(25*'=')
print('')

Triângulo = float(TrianguloA) *  float(TrianguloB) / 2.0 
Circulo = 3.1415 * float(CirculoA) * float(CirculoA)
Trapezio = ( float(TrapezioA)+float(TrapezioB)) / 2.0 * float(TrapezioC)
Quadrado = float(QuadradoA) * float(QuadradoA)
Retangulo = float(RetanguloA) * float(RetanguloB)

print(f'A área do Triangulo é {Triângulo}')
print(f'A área do Circulo é {Circulo}')
print(f'A área do Trapézio é {Trapezio}')
print(f'A área do Quadrado é {Quadrado}')
print(f'A área do Retangulo é {Retangulo}')


