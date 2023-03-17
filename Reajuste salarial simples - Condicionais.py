salario = float(input('Qual valor do salário?'))
if salario <= 1250:
    reajuste = salario * 1.15
else:
    reajuste = salario *1.1
print('Após reajuste seu salário é: R${:.2f}.'.format(reajuste))