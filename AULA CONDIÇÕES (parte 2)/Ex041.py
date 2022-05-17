from datetime import date

ano = date.today().year
print('\033[34m---' * 15)
nasc = int(input('Qual a data de nascimento do atleta?\n'))
print('---' * 18)
idade = ano - nasc
if idade <= 9:
    print('Você foi cadastrado com sucesso na categoria mirim!')
    print('---' * 18)
elif 9 < idade <= 14:
    print('Você foi cadastrado com sucesso na categoria infantil!')
    print('---' * 18)
elif 14 < idade <= 19:
    print('Você foi cadastrado com sucesso na categoria junior!')
    print('---' * 18)
elif idade == 20:
    print('Você foi cadastrado com sucesso na categoria sênior!')
    print('---' * 18)
else:
    print('Você foi cadastrado com sucesso na categoria master!')
    print('---' * 18)
