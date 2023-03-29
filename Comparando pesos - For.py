print('__'*17+'\nCOMPARANDO PESOS\n'+'__'*17)

peso = 0
maior = 0
menor = 0
for i in range (1,6,1):
    peso = float(input(f'Peso da {i}ª pessoa:'))
    if i == 1:
        maior = peso
        menor = peso
    else:  
        if maior < peso:
            maior = peso
            
        if menor > peso:
            menor = peso
    
print (f'O maior peso lido foi {maior:.2f}kg.')
print (f'O menor peso lido foi {menor:.2f}kg.')