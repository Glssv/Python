distancia= float(input('qual é a distancia da sua viagem?'))
print('você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço= distancia* 0.50
else:
    preço= distancia * 0.45
print('e preço da sua passagem será de r${:.2f}'.format(preço))