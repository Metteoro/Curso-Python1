from random import randint
num = randint(1, 3)
print('\033[33m-='*17)
print('\033[35mVAMOS JOGAR PEDRA, PAPEL OU TESOURA?')
print('\033[33m-='*17)
jokenpo = str(input('\033[35mO QUE VOCÊ VAI JOGAR ?')).upper().strip()
ppt = ['TESOURA', 'PEDRA', 'PAPEL', 'TESOURA', 'PEDRA']
if jokenpo == 'PEDRA':
    jokenpo = 1
if jokenpo == 'PAPEL':
    jokenpo = 2
if jokenpo == 'TESOURA':
    jokenpo = 3
if num == jokenpo:
    print('\033[33m-=' * 17)
    print(f'\033[35mEU ESCOLHI {ppt[num]} E VOCÊ ESCOLHEU {ppt[jokenpo]}.')
    print('QUE CHATO! FOI EMPATE!')
    print('\033[33m-=' * 17)
elif num+1 == jokenpo:
    print('\033[33m-=' * 17)
    print(f'\033[35mEU ESCOLHI {ppt[num]} E VOCÊ ESCOLHEU {ppt[jokenpo]}.')
    print(f'QUE CHATO!! EU PERDI ;-;')
    print('\033[33m-=' * 17)
else:
    print('\033[33m-=' * 17)
    print(f'\033[35mEU ESCOLHI {ppt[num]} E VOCÊ ESCOLHEU {ppt[jokenpo]}.')
    print(f'AS MAQUINAS SÃO MELHORES, EU GANHEI!')
    print('\033[33m-=' * 17)
