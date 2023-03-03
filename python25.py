n1= float(input('digite a sua primeira nota'))
n2= float(input('digite sua segunda nota'))
m= (n1 + n2)/2
print('sua nota foi {:.1f}'.format(m))
if m >= 6.0:
    print('você está na media parabens')
else:
    print('você não está na media, estude mais')