# Criando e ordenando lista
lista = []
lista.append(int(input('Digite um valor: ')))
continuar = 'S'
while continuar != 'N':
    continuar = input('Quer continuar [ S / N ]: ').upper()
    if continuar != 'N':
        lista.append(int(input('Digite um valor: ')))
ordenada = []
for i in range(len(lista)):
    menor = lista[0]
    for j in range(len(lista)):
        if menor > lista[j]:
            menor = lista[j]
    ordenada.append(menor)
    lista.remove(menor)

lista = ordenada
print(lista)