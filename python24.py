n= str(input('qual o seu nome completo?')).strip()
nome= n.split()
print('é um prazer te conhecer!')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
