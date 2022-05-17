from time import sleep
from random import randint
print("-="*15)
print("VAMOS JOGAR PAR OU IMPAR")
print("-="*15)
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    parimpar = str(input("Par ou impar?")).upper().strip()[0]
    while parimpar not in "PI":
        parimpar = str(input("Por favor escolha par ou impar: ")).upper().strip()[0]
    computador = randint(1, 10)
    if parimpar == "P" and (computador + valor) % 2 == 0:
        cont += 1
        print("Você ganhou vamos jogar denovo ?")
    elif parimpar == "I" and (computador + valor) % 2 != 0:
        cont += 1
        print("Você ganhou vamos jogar denovo ?")
    else:
        print(f"Você perdeu!")
        if cont > 1:
            print(f"Você ganhou {cont} vezes!")
        elif cont == 1:
            print(f"Você ganhou {cont} vez!")
        break
