from datetime import date
ano_a = date.today().year
velhos = 0
novos = 0
nasc = 0
for c in range(0, 7):
    nasc = int(input(f"Em que ano nasceu a {c+1}° pessoa? "))
    if nasc+18 > ano_a:
        novos += 1
    else:
        velhos += 1
print(f"Dessas pessoas {velhos} são maiores de idade e {novos} são menores.")