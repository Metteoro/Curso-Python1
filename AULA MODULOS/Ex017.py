import math
a = float(input('Qual o comprimento do primeiro lado do triangulo? '))
b = float(input('Qual o comprimento do segundo lado do triangulo? '))
c = math.hypot(a,b)
print(f'O valor da hipotenusa desse triangulo é {c:.2f}.')
