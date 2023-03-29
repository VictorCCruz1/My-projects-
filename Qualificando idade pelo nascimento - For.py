print('__'*17+'\nQUALIFICANDO IDADE PELO NASCIMENTO\n'+'__'*17)
from time import gmtime

atual = gmtime()[0]
maiores = 0
menores = 0

for i in range(0,7,1):
    idades = int(input('Digite a idade: '))
    final = atual - idades
    if final < 18:
        menores += 1
    elif final >= 18:
        maiores += 1

print(f'O total de menores de idade foi de {menores}.')
print (f'O total de maiores de idade foi de {maiores}.')
  