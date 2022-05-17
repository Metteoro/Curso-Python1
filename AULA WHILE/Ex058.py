from random import randint
num = randint(1,10)
print(num)
chute = int(input("Estou pensando em um número de 1 a 10, tente adivinhar: "))
tentativas = 1
while num != chute:
    chute = int(input("Você errou!\n Vou te dar outra chance, que número eu estou pensando? "))
    tentativas += 1
if tentativas == 1:
    print("Parabéns você acertou de primeira!")
else:
    print(f"Você precisou de {tentativas} tentativas pra acertar!")
