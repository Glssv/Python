import random
n1= input('nome do primeiro aluno')
n2= input('nome o segundo aluno')
n3= input('nome do terceiro aluno')
n4= input('nome do quarto aluno')
lista= [n1,n2,n3,n4]
escolhido= random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))