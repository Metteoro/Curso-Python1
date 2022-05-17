import math
alpha = float(input('Digite um angulo em graus: '))
sen = math.sin(math.radians(alpha))
cos = math.cos(math.radians(alpha))
tan = math.tan(math.radians(alpha))
print(f'O seno desse angulo é {sen:.2f}')
print(f'O cosseno desse angulo é {cos:.2f}')
print(f'A tangente desse angulo é {tan:.2f}')
