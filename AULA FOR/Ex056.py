contm = 0
somai = 0
nomev = ''
idadev = 0
for p in range(1, 5):
    print(f"~~~~~~ {p}° PESSOA ~~~~~~")
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    somai += idade
    if idade > idadev and sexo == "M":
        idadev = idade
        nomev = nome
    if idade < 20 and sexo == "F":
        contm += 1
media = somai/4
print(f"A média de idade dessas pessoas é {media}.")
print(f"O nome do homem mais velho é {nomev}.")
print(f"O número de mulheres com menos de 20 anos é {contm}.")
