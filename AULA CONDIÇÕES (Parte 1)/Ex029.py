print("\033[33m-"*30)
print("\033[33mRADAR DE VELOCIDADE A FRENTE !!")
print("\033[33m-"*30)
vel = float(input('\033[33mQual a velocidade do seu carro? '))
if vel >= 80:
    print("\033[31m-\033[m" * 55)
    print(f'\033[31mVOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE!!!\033[m')
    print(f"\033[31mVOCE TERÁ QUE PAGAR UMA MULTA NO VALOR DE {(vel-80)*7:.2f}R$!")
    print("\033[31m-\033[m" * 55)
else:
    print("\033[32m-" * 45)
    print('\033[32mVOCÊ ESTÁ DENTRO DA VELOCIDADE PERMITIDA !')
    print("\033[32m-" * 45)
