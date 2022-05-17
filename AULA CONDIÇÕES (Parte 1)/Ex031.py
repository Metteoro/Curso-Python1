dist = float(input('Qual a distância da sua viagem ?'))
if dist <= 200:
    print(f"O valor da sua passagem é {dist*0.5}.")
else:
    print(f"O valor da sua passagem é {dist*0.45}")
