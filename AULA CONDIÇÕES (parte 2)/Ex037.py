print('\033[35m~~~'*20)
print('BEM-VINDO! EU SOU JERBAS, SEU CONVERSOR NUMÉRICO DIGITAL!')
print('\033[35m~~~'*20)
tipo = int(input('''ESCOLHA A OPÇÃO DE CONVERSÃO DESEJADA 
[ 1 ] BINÁRIO
[ 2 ] OCTAL 
[ 3 ] HEXADECIMAL.\n'''))
print('~~'*20)
num = int(input('QUAL NÚMERO VOCÊ DESEJA CONVERTER ?\n'))
print('~~'*20)
if tipo == 1:
    print(f'O número {num} convertido em binário é igual a {bin(num)[2:]}')
elif tipo == 2:
    print(f'O número {num} convertido em octal é igual a {oct(num)[2:]}')
elif tipo == 3:
    print(f'O número {num} convertido em octal é igual a {hex(num)[2:]}')
else:
    print("Por favor insira uma opção válida de  ")
