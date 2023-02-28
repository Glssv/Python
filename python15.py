from math import hypot
co= float(input('numero do cateto oposto '))
ca= float(input('numerodo  cateto adjacente '))
hi= hypot(co,ca)
print('a hipotenusa é {:.2f}'.format(hi))