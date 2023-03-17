distancia = float(input('Qual distancia da viagem em km? '))
if distancia > 200:
    preço = ('O valor da viagem é de R${:.2f}.'.format(distancia*0.45))
else:
    preço = ('O valor da viagem é de R${:.2f}.'.format(distancia*0.5))
print(preço)
