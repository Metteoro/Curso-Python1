sexo = str(input("Qual o seu sexo[M/F] ? ")).strip().upper()
while sexo != ("M" and "F"):
    print(f"{sexo} não corresponde a um sexo válido.")
    sexo = str(input("Por favor digite um sexo válido[M/F}:")).strip().upper()
print(sexo)
