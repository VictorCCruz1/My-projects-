print('=-'*17+'\nDESCOBRINDO SE O NÚMERO É PRIMO\n'+'=-'*17)

numero  = int(input('Digite o número a ser analisado: '))
qnt = 0
if 0 != numero != 1:
    print('O número é divisível por',end='')
    for i in range(1, numero+1, 1):
        if numero % i == 0:
            qnt += 1
            if qnt == 2:
              mensagem = (f' {qnt} números, então {numero} é primo!')
            else:
              mensagem = (f' {qnt} números, então {numero} não é primo!')
else:
   mensagem = (f'O número {numero} não se enquadra como composto ou primo.')
print(mensagem)