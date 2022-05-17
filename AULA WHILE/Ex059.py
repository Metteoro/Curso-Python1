from time import sleep
resultado = 0
opcao = 0
print("Digite dois números")
num1 = float(input("Primeiro: "))
num2 = float(input("Segungo: "))
while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] MUDAR OS NÚMEROS
    [5] FINALIZAR''')
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        resultado = num1 + num2
        print(f"O resultado da soma de {num1} e {num2} é {resultado}.")
    elif opcao == 2:
        resultado = num1 * num2
        print(f"O resultado da multipicação de {num1} por {num2} é igual a {resultado}")
    elif opcao == 3:
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
        print(f"O maior número entre {num1} e {num2} é {resultado}")
    elif opcao == 4:
        print("Digite os número novamente:")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print("OPÇÃO INVÁLIDA DIGITE NOVAMENTE...")
print("FIM DO PROGRAMA")
