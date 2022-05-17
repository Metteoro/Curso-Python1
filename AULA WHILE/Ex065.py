soma = 0
media = 0
cont = 0
maior = 0
menor = 0
parar = ""
while parar != "P":
    num = float(input("Digite um número: "))
    if cont == 0:
        menor = maior = num
    else:
        if menor > num:
            menor = num
        elif maior < num:
            maior = num
    soma += num
    cont += 1
    parar = str(input("Você deseja continuar ou parar [C/P] ?")).upper().strip()
media = soma / cont
print(f"Você digitou {cont} números e a media foi {media}.")
print(f"Além disso o menor número foi {menor} e o maior foi {maior}.")
