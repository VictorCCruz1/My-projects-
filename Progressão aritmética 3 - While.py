print('__'*17+'\nPROGRESSÃO ARITIMÉTICA 3\n'+'__'*17) 

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

x = 1
print(f'{n} ➡', end='')
while x < 10:
    x += 1
    n += r
    print(f'  {n} ➡', end='')
print('  PAUSA')

y = int(input('Quantos termos mais: ')) + x
while y != x:
    while x < y:
        x += 1
        n += r
        print(f'  {n} ➡', end='')
    print('  PAUSA')
    y = int(input('Quantos termos mais: ')) + x
    
print(f'Foi finalizado com total de termos: {x}.')