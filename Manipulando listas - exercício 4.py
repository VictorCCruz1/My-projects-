#   4. Faça um programa que percorre duas listas e intercala os elementos
#   de ambas, formando uma terceira lista. A terceira lista deve começar
#   pelo primeiro elemento da lista menor.
#   
#   Exemplo:
#   lista1 = [1, 2, 3, 4]
#   lista2 = [10, 20, 30, 40, 50, 60]
#   lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]

lista_x = [1, 2, 3, 4]
lista_y = [10, 20, 30, 40, 50, 60]
lista1 = []
lista2 = []

if (len(lista_x)) < (len(lista_y)):
    lista1 += lista_x
    lista2 += lista_y
else:
    lista1 += lista_y
    lista2 += lista_x

lista_final = []
for i in range(len(lista1)+len(lista2)):
    if i < (len(lista1)):
        lista_final.append(lista1[i])
        lista_final.append(lista2[i])
    if len(lista1) <= i and i < len(lista2):
        lista_final.append(lista2[i])

print(lista_final)
             