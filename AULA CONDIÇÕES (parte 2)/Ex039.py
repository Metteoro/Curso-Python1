from datetime import date
ano = date.today().year
print('\033[33m~~'*18)
print('\033[32mSAIBA QUANDO VOCÊ DEVERÁ SE ALISTAR')
print('\033[33m~~'*18)
nasc = int(input('\033[32mEM QUE ANO VOCÊ NASCEU?\n'))
if ano-nasc == 18:
    print('\033[33m~~' * 25)
    print("\033[32mPARABENS!! ESTÁ NA HORA DE CUMPRIR SEU DEVER")
    print("ALISTE-SE JÁ")
    print('\033[33m~~' * 25)
elif ano-nasc > 18:
    print('\033[33m~~' * 20)
    print("\033[32mJÁ PASSOU DO TEMPO DE SE ALISTAR!!")
    print("CONFIRA SUA SITUAÇÃO NO SITE DO EXERCITO")
    print('\033[33m~~' * 20)
else:
    if (18 - (ano - nasc)) == 1: x='ANO'
    else: x='ANOS'
    print('\033[33m~~' * 28)
    print(f"\033[32mFIQUE TRANQUILO, AINDA FALTAM {18-(ano-nasc)} {x} PARA O ALISTAMENTO. ")
    print('\033[33m~~' * 28)