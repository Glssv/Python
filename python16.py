import math
angulo= float (input('digite o angulo que vc deseja'))
seno= math.sin(math.radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
coss= math.cos(math.radians(angulo))
print('o angulo {} tem o cosseno de {:.2f}'.format(angulo,coss))
tang= math.tan(math.radians(angulo))
print('o angulo {} tem a tangente de {:.2f}'.format(angulo,tang))