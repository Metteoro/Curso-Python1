print('Digite as notas do aluno:')
n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
m = (n2+n1)/2
if m < 5:
    print(f'\033[31mSua média foi {m}.')
    print('Infelizmente você reprovou!')
elif 5 <= m < 7:
    print(f'\033[33mSua média foi {m}.')
    print("Você está de recuperação! Estude mais!")
else:
    print(f'\033[32mSua média foi {m}.')
    print("PARABÉNS!!! VOCÊ ESTÁ APROVADO!!!")