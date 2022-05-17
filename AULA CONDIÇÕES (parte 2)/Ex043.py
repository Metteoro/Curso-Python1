print("\033[35m-_-" * 5)
print("TESTE DE IMC")
print("-_-" * 5)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
asp = str('')
if imc < 18.5:
    print("\033[33m-_-" * 15)
    print(f'\033[33mSeu IMC é {imc:.2f}.')
    print("Cuidado! Você está abaixo do peso ideal.")
    print("\033[33m-_-" * 15)
elif 18.5 <= imc < 25:
    print("\033[32m-_-" * 15)
    print(f'\033[32mSeu IMC é {imc:.2f}.')
    print(f'Fique tranquilo! Você está dentro do peso ideal.')
    print("\033[32m-_-" * 15)
elif 25 <= imc < 30:
    print("\033[33m-_-" * 15)
    print(f'\033[33mSeu IMC é {imc:.2f}.')
    print("Cuidado! Você está com sobrepeso.")
    print("\033[33m-_-" * 15)
elif 30 <= imc < 40:
    print("\033[31m-_-" * 15)
    print(f'\033[31mSeu IMC é {imc:.2f}.')
    print("Cuidado! Você está obeso.")
    print("\033[31m-_-" * 15)
else:
    print("\033[31m-_-" * 15)
    print(f'\033[31mSeu IMC é {imc:.2f}.')
    print("Cuidado!!! Você está com obesidade morbida.")
    print('Proucure ajuda médica!')
    print("\033[31m-_-" * 15)
