from datetime import date
ano= int(input('que ao quer analisar? Coloque 0 pra analisar o ao atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
        print('o ano {} é bissexto'.format(ano))
else:
    print('o  NÃO é bissexto ao {}'.format(ano))