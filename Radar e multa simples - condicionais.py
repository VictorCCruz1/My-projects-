velocidade = float(input('Velocidade do carro: '))
if velocidade <= 80:
    mensagem = 'OK, dirija com cuidado!'
else:
    multa = ((velocidade//1)-80)*7
    mensagem = ('Você está acima do limite, sua multa é de R${:.2f}.'.format(multa))
print(mensagem)