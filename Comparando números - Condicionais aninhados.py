print('\nCOMPARANDO NÚMEROS\n'+'=-'*20)

n1 = int(input('Qual primeiro número:'))
n2 = int(input('Qual segundo número:'))

if n1 > n2:
    mensagem = ('O primeiro número é o maior valor.')
elif n1 < n2:
    mensagem = ('O segundo número é o maior valor.')
else:
    mensagem = ('Os números são iguais.')

print(mensagem)
