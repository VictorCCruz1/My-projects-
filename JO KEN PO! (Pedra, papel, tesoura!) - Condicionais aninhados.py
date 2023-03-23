import random
from time import sleep
print('\n\nJO KEN PO!\n'+'=-'*15)
op_pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('\nEscolha uma opção:\n')
op_user = int(input('[ 1 ] para PEDRA\n'
                  '[ 2 ] para PAPEL\n'
                  '[ 3 ] para TESOURA\n'
                  'R:'))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

if op_user == 1:
    if op_pc == 'TESOURA':
        mensagem = (f'A opção do compurador foi {op_pc},\n VOCÊ GANHOU!')
    elif op_pc == 'PAPEL':
        mensagem = (f'A opção do compurador foi {op_pc},\n VOCÊ PERDEU!')
    elif op_pc == 'PEDRA':
        mensagem = (f'A opção do compurador foi {op_pc},\n DEU EMPATE!')

elif op_user == 2:
    if op_pc == 'TESOURA':
        mensagem = (f'A opção do compurador foi {op_pc},\n VOCÊ PERDEU!')
    elif op_pc == 'PAPEL':
        mensagem = (f'A opção do compurador foi {op_pc},\n DEU EMPATE!')
    elif op_pc == 'PEDRA':
        mensagem = (f'A opção do compurador foi {op_pc},\n VOCÊ GANHOU!')

elif op_user == 3:
    if op_pc == 'TESOURA':
        mensagem = (f'A opção do compurador foi {op_pc},\n DEU EMPATE!')
    elif op_pc == 'PAPEL':
        mensagem = (f'A opção do compurador foi {op_pc},\n VOCÊ GANHOU!')
    elif op_pc == 'PEDRA':
        mensagem = (f'A opção do compurador foi {op_pc},\n VOCÊ PERDEU')

else:
    mensagem = ('\n\nERRO!\n')

print(f'\n{mensagem}\n')
