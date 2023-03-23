a = 0
qnt = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        qnt += 1
        a +=  i
print(f'O valor do somatório dos {qnt} números é {a}.')