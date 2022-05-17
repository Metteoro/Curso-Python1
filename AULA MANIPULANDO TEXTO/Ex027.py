nome = str(input('Digite seu nome completo: ')).strip()
spci = nome.find(" ")+1
spcf = nome.rfind(" ")+1
print(f"Seu primeiro nome é {nome[:spci]}")
print(f"Seu ultimo nome é {nome[spcf:]}")