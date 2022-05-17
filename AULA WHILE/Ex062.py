contador = 0
ptermo = float(input("Qual o primeiro termo da PA ? "))
razao = float(input("Qual a razão da PA ? "))
termos = 10
while contador != termos:
    ptermo += razao
    contador += 1
    print(f"O {contador} termo dessa pa é {ptermo}")
cont = str(input("Você deseja ver mais termos dessa PA [S/N]? ")).strip().upper()[0]
if cont == "S":
    termos += int(input("Quantos termos você ainda deseja ver ? "))
    while contador != termos:
        ptermo += razao
        contador += 1
        print(f"O {contador} termo dessa pa é {ptermo}")
print("Fim")
