nome = str(input('Digite seu nome completo: ')).upper().strip()
print('Seu nome tem Silva ?')
print(f'{nome.count("SILVA") != 0}')