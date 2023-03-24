print('=-'*17+'\nTABUADA\n'+'=-'*17)

n = int(input('deseja a tabuada de qual número? '))
print('=-'*17)
for i in range(1, 11, 1):
    m = i*n
    print(f' {n} x {i:2} = {m} ')
print('=-'*17)