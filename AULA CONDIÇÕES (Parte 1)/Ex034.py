sal = float(input("Digite o seu salário para saber o valor do aumento salarial: "))
if sal >= 1250:
    print(f"O valor do seu aumento é {sal*0.1:.2f}R$.")
else:
    print(f"O valor do seu aumento é {sal*0.15:.2f}R$.")
