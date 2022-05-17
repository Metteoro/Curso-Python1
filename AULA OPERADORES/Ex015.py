dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quando Km foram rodados no carro? '))
al = (dias*60)+(km*0.15)
print(f'O valor do aluguel é {al:.2f}R$')