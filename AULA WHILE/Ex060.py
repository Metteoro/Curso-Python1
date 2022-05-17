num = int(input("Digite um número: "))
fatorial = 1
contador = 1
while contador != num+1 :
    fatorial *= contador
    contador += 1
print(f"O fatorial de {num} é {fatorial}")
