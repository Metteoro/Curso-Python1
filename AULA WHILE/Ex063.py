termos = int(input("Quantos termos da sequencia você deseja ver ? "))
fibonacci = 0
fibonacci2 = 1
cont = 0
while termos != cont:
    print(f"O {cont} termo da sequencia de fibonacci é {fibonacci}")
    fibonacci3 = fibonacci + fibonacci2
    fibonacci = fibonacci2
    fibonacci2 = fibonacci3
    cont += 1
