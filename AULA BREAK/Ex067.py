print("=-="*6)
print("TABUADA")
print("=-="*6)
while True:
    num = int(input("Digite um número:"))
    if num < 0:
        break
    for c in range(1,11):
        tabuada = c * num
        print(f"{num:2} x {c:2} = {tabuada}")

print("FIM DO PROGRAMA.")
