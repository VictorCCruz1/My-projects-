#   3. Faça um programa que percorre um vetor e imprime na tela o valor
#   mais próximo da média dos valores do vetor. Exemplo:
#   
#   vetor = [2.5, 7.5, 10.0, 4.0]
#   (média = 6.0)
#   Valor mais próximo da média = 7.5
tamanho = int(input('Qual tamanho da lista: '))
vetor = []
soma = 0

for i in range(tamanho):
    vetor.append(float(input('Inserir o valor: ')))

for i in range(len(vetor)):
    soma += vetor[i]
media = (soma) / len(vetor) 
print(f'(media = {media:.1f})')

for i in range(len(vetor)):
    resto1 = vetor[i] - media
    if resto1 < 0:
        resto1 = resto1 * (-1)
    for j in range(len(vetor)):
        resto2 = vetor[j] - media
        if resto2 < 0:
            resto2 = resto2 * (-1)
        if resto2 < resto1:
            proximo = vetor[j]
print(f'Valor mais próximo da média = {proximo}')