'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
'''

i = 1
j = 7

while True:
    g = 0
    for c in range(3):
        print('I={} J={}'.format(i, j-g))
        g += 1

    if i == 9:
        break
    else:
        i += 2
        j += 2
