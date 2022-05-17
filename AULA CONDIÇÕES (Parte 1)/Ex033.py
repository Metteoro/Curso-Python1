print("Digite 3 números para saber qual o maior: ")
a = float(input("Primeiro: "))
b = float(input("Segundo: "))
c = float(input("Terceiro: "))
menor=a
if a > b and c > b:
    menor = b
if b > c and b > c:
    menor = c
maior=c
if c < b and a < b:
    maior = b
if b < a and c < a:
    maior = a
print(f"O maior valor é {maior}.")
print(f"O menor valor é {menor}")