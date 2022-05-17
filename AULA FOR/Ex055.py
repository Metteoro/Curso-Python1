menor = 0
maior = 0
peso = 0
for p in range(1,6):
    peso = float(input(f"Peso da {p} pessoa: "))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if menor > peso:
            menor = peso
        elif maior < peso:
            maior = peso
print(f"O maior peso foi {maior}kg.")
print(f"O menor peso foi {menor}kg.")
