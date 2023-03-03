nome= str(input('digite uma frase')).lower().strip()
print('a letra A aparce {} vezes nessa frase'.format(nome.count('a')))
print('a primeira letra A apareceu na posição {}'.format(nome.find('a')+1))
print('a ultima letra A apareceu na posição {}'.format(nome.rfind('a')+1))