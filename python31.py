salario= float(input('qual é o salario do funcionario?'))
if salario <= 1200:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava R${:.2f} agora passa a ganhar R${:.f2}'.format(salario, novo))