print('__'*17+'\nPROGRESSÃO ARITIMÉTICA 2\n'+'__'*17) 

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
x = 0
print(f'{n} ➡', end='')
while x != 9:
    x += 1
    n += r
    print(f'  {n} ➡', end='')

print('  FIM')