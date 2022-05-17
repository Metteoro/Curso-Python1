num = int(input('Qual número você deseja saber a tabuada?\n'))
print(f'TABUADA DO {num}')
for c in range(1, 11):
    print(f"{num} X {c:2} = {num*c}")
