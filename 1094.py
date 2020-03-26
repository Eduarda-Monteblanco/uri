'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''
n = int(input())
total = coelho = rato = sapo = 0
for i in range(n):
    valores = input().split()
    quantia = int(valores[0])
    tipo = str(valores[1])

    total += quantia

    if tipo == 'C':
        coelho += quantia
    elif tipo == 'R':
        rato += quantia
    elif tipo == 'S':
        sapo += quantia

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format((coelho*100)/total))
print('Percentual de ratos: {:.2f} %'.format((rato*100)/total))
print('Percentual de sapos: {:.2f} %'.format((sapo*100)/total))
