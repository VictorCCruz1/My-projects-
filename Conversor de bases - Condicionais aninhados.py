print('CONVERSOR DE BASES NUMÉRICAS')
print('=-'*20+'=')
print('''Escolha uma opção:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
n = int(input('Escolha seu número:'))
o = int(input('Qual sua opção:'))

if o == 1:
    mensagem = ('O número {} na base binária é {}.'.format(n, bin(n)[2:]))

elif o == 2:
    mensagem = ('O número {} na base octal é {}.'.format(n, oct(n)[2:]))

elif o == 3:
    mensagem = ('O número {} na base hexadecimal é {}.'.format(n, hex(n)[2:]))

else:
    mensagem = ('Dados incorretos, tente novamente.')

print(mensagem)