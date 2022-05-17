import random
from time import sleep
lista = [0, 1,  2, 3, 4, 5]
num1 = random.randint(0, 5)
print("\033[33m-=-"*20)
print('\033[31mVou pensar em um numero de 0 a 5. Tente adivinhar! ')
print("\033[33m-=-"*20)
num2 = int(input("\033[34mEscolha um numero: "))
print("\033[33m-=-"*20)
print('\033[31mPROCESSANDO...')
sleep(2.5)
if (num1 == num2):
    print("\033[33m-=-" * 20)
    print('\033[32mParabens você ganhou!')
    print("\033[33m-=-" * 20)
else:
    print("\033[33m-=-" * 20)
    print(f'\033[31mVocê perdeu, eu escolhi o numero {num1}!')
    print("\033[33m-=-" * 20)