print('Digite os lados do triângulo:')
n1 = float(input('Primeiro lado: '))
n2 = float(input('Segundo lado: '))
n3 = float(input('Terceiro lado: '))
if n1 >= n2 + n3 or n2 >= n1 + n3 or n3 >= n2 + n1:
    print('Esse triangulo não pode existir!')
else:
    if (n1 == n2 or n1 == n3 or n2 == n3) and (n1 == n2 == n3) == False:
        print(f'O triangulo {n1}, {n2}, {n3} é isósceles!')
    elif n1 == n2 == n3:
        print(f'O triangulo {n1}, {n2}, {n3} é equilátero!')
    else:
        print(f'O triangulo {n1}, {n2}, {n3} é escaleno!')
