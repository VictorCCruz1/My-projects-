#    2. Faça um programa que simule um lançamento de dados. Lance o
#    dado 10 vezes e armazene os resultados em um vetor. Depois, monte
#    um outro vetor contendo quantas vezes cada valor foi obtido. Imprima
#    os dois vetores. Use uma função para gerar números aleatórios,
#    simulando os lançamentos dos dados.
#    
#    Exemplo de uma possível saída:
#    [3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
#    [1, 0, 3, 1, 4, 1]

import random
lista = []
lista_rep = []
for a in range(10):
    x = random.randint(1,6)
    lista.append(x)
for i in range(1,7):
    n = i
    rep = 0
    for j in (lista):
        if n == j:
            rep+=1
    lista_rep.append(rep)
print(' Lançamentos do dado: ',f'{lista}\n','Repetições: ' ,f'{lista_rep}')
