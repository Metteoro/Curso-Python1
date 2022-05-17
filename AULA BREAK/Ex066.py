soma = 0
quant = 0
num = 0
while True:
    num = float(input(f"Digite um valor (Para parar digite 999): "))
    if num == 999:
        break
    soma += num
    quant += 1
print(f"A soma desses valores foi {soma} e você digitou {quant} valor. ")
