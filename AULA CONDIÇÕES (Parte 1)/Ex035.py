print("Digite 3 medidas para saber se é possivel formar um triangulo com elas:")
a = float(input("Primeira: "))
b = float(input("Segunda: "))
c = float(input("Terceira: "))
if (a-b+c) > 0 and (b+a-c) > 0 and (c-a+b) > 0:
    print("Esse triangulo é possivel.")
else:
    print("Esse triangulo não é possivel.")