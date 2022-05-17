pa = int(input("Digite o primeiro termo da PA: "))
rz = int(input('Digite a razao dessa PA: '))
for c in range(0, 10):
    print(f"O {c+1:2}° termo da PA é {pa:2}.")
    pa += rz
