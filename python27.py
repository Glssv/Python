velocidade= float(input('qual é a velocidade atual do carro?'))
if velocidade >80:
    print('multado! você excedeu o limite de segurança que é de 80km/h')
    multa= (velocidade-80) *7
    print('você deve pagar uma multa de {:.2f}'.format(multa))
print('tenha um bom dia! Dirija com segurança')