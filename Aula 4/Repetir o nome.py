nome = input('Digite o seu nome: ')
repetir = int( input("Digite o numero de vezes que você quer seu nome na tela: " ))
contador = 1 


while contador <= repetir:
    print(f"Sr(a) {nome}, estamos na {contador}ª repetição!")
    contador += 1