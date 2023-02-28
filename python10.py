l=float(input('qual a largura da parede'))
a= float(input('qual a altura da parede'))
area= l*a
print('sua parede tem a dimenção de {}x{} e sua área é de {}'.format(l,a,area))
print('pra pintar a parede você precisará de {}l de tinta'.format(area/2))