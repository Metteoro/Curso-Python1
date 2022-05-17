print('\033[33m---'*15)
print('PAGAMENTO:')
print('1. À VISTA NO DINHEIRO/PIX: 10% DE DESCONTO')
print('2. À VISTA NO CARTÃO: 5% DE DESCONTO')
print('3. EM 2X NO CARTÃO SEM JUROS')
print('4. EM 3X OU MAIS NO CARTÃO COM JUROS DE 15%')
print('\033[33m---'*15)
opc = int(input('Digite a opção de pagamento desejada: '.upper()))
p = float(input('Digite o valor do produto: '.upper()))
if opc == 4:
    nump = int(input('Qual o número de parcelas? '.upper()))
if opc == 1:
    print('\033[33m---'*15)
    print(f"O valor à ser pago é {p*0.9:.2f}R$.".upper())
    print('\033[33m---'*15)
elif opc == 2:
    print('\033[33m---' * 15)
    print(f"O valor à ser pago é {p * 0.95:.2f}R$.".upper())
    print('\033[33m---' * 15)
elif opc == 3:
    print('\033[33m---' * 15)
    print(f"O valor à ser pago é {p/2:.2f}R$ em 2x sem juros.".upper())
    print('\033[33m---' * 15)
elif opc == 4:
    print('\033[33m---' * 15)
    print(f"O valor à ser pago é {(p * 1.15)/nump:.2f}R$ em {nump}x.".upper())
    print('\033[33m---' * 15)