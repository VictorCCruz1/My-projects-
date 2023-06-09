# Inserindo valores me uma lista de tamanho selecionado, analisando, obtendo índices dos anasilados.

lista = []
entradas = int(input( 'Quantas entradas deseja realizar? ')) #determinando tamanho da lista
while entradas < 1:
    entradas = int(input( 'Quantas entradas (maior que zero) deseja realizar?')) 
for k in range(entradas):
    lista.append(int(input('Digite um valor: '))) #inserindo valores na lista
print(lista)

for i in range(len(lista)):
    temp = lista[i] #variável temporária na posição i da lista
    if i == 0:
        valor_alto = lista[i]   # iniciando o primeiro valor da lista para comparações de valor alto
        valor_baixo = lista[i]  # o mesmo para o valor baixo
    else:
        if temp > valor_alto: # compara e muda variável caso o valor atual analisado seja maior
            valor_alto = temp
        if temp < valor_baixo:  # o mesmo para o menor
            valor_baixo = temp

lista_alto = []
for i in range(len(lista)): #criando uma lista com as posições do valor mais alto    
    if lista[i] == valor_alto:
        lista_alto.append(i)

lista_baixo = []
for i in range(len(lista)): #o mesmo para os valores mais baixos
    if lista[i] == valor_baixo:
        lista_baixo.append(i)
        
print(f'O valor mais alto foi {valor_alto}, encontrado no(s) índice(s): {lista_alto}.')
print(f'O valor mais baixo foi {valor_baixo}, encontrado no(s) índice(s): {lista_baixo}.')