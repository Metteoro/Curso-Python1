soma = 0
quant = 0
num = 0
while num != 999:
    num = float(input(f"Digite um número (Parar o programa digite 999): "))
    if num != 999:
        soma += num
        quant += 1
print(f"A soma desse número foi {soma} e você digitou {quant} números. ")
