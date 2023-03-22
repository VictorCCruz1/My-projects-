print('\n\nCÁLCULO IMC\n'+'=-'*15)

peso = float(input('Digite sua massa corporal(kg):'))
altura = (float(input('Digite sua altura(metro):')))**2

imc = (peso/altura)
imc_str = (str(imc))[0:5]

if imc < 18.5:
    mensagem = (f'Seu imc {imc_str} classifica-o como abaixo do peso.')

elif 18.5 <= imc < 25:
    mensagem = (f'Seu imc {imc_str} classifica-o como peso ideal.')

elif 25 <= imc < 30:
    mensagem = (f'Seu imc {imc_str} classifica-o como em sobrepeso.')

elif 30 <= imc < 40:
    mensagem = (f'Seu imc {imc_str} classifica-o como em obesidade.')

elif imc > 40:
    mensagem = (f'Seu imc {imc_str} classifica-o como em obesidade, mórbida')

print(mensagem)