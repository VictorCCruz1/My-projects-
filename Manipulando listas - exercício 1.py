# Manipulando listas - exercício 1
#   1. Faça um programa que percorre uma lista com o seguinte formato:
#      [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha',
#      [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. 
#      Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a
#      Itália fez 9. O programa deve imprimir na tela:
#      (a) o total de faltas do campeonato
#      (b) o time que fez mais faltas
#      (c) o time que fez menos faltas

lista = [['Brasil', 'Italia', [10, 9]], ['Alemanhã', 'Espanha', [5, 7]], ['Italia', 'Espanha',[7,8]]]
total_faltas = maior = 0
faltas = []

for i in range(len(lista)):
    faltas.append([])
    for j in (lista[i][2]):
        faltas[i].append(j)
        total_faltas += j
    for l in range(len(lista[i][2])): 
        temp0 = lista[i][2][l]
        if maior < temp0:
            maior = temp0
            time_mais = lista[i][lista[i][2].index(maior)]
    for k in range(len(lista[i][2])): 
        temp1 = lista[i][2][k]
        if lista[i][2][k] == lista[0][2][0]:
            menor = lista[i][2][k]
        else:
            if menor > temp1:
                menor = temp1
                time_menos = lista[i][lista[i][2].index(menor)]  

print(f'O total de faltas da rodada foi: {total_faltas}.')
print(f'O time que mais cometeu faltas foi: {time_mais}.')
print(f'O time que menos cometeu faltas foi: {time_menos}.')