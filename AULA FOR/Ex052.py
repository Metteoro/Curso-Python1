num = int(input('Digite um número para saber se ele é primo: '))
mult = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end='')
        mult += 1
    else:
        print('\033[34m', end='')
    print(c, end=' ')
print('\033[m')
if mult == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O numero {num} não é primo.")