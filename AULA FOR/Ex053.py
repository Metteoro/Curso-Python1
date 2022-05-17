frs = str(input("Digite uma frase: ")).strip().upper()
palavras = frs.split()
junto = "".join(palavras)
print(f"A frase {junto} ao contrario se escreve {junto[::-1]}")
if junto == junto[::-1]:
    print("E essa frase é um palindromo.")
else:
    print("E essa frase não é um palindromo.")