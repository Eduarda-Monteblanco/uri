'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo
'''

i = 1
j = 60

while True:

    print('I={} J={}'.format(i, j))

    if j == 0:
        break
    else:
        i += 3
        j -= 5