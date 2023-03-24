print('=-'*17+'\nPROGRESSÃO ARITIMÉTICA\n'+'=-'*17)

termo1 = int(input('Digite o primeiro termo: '))
razao  = int(input('Digite a razão entre os temos: '))
for i in range(termo1, termo1+(10*razao), razao):
    print(f' {i:2}', end='➡')
print(' acabou!')