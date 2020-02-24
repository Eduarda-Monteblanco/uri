<<<<<<< HEAD
'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
'''
import math
a,b,c = map(float, input().split())

delta = (b*b) - 4*a*c
if delta < 0:
    print('Impossivel calcular')
elif a == 0:
    print('Impossivel calcular')
else:
    x1 = ((b*-1) + math.sqrt(delta))/(2*a)
    x2 = ((b*-1) - math.sqrt(delta))/(2*a)
    print('R1 = {:.5f}'.format(x1))
=======
'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
'''
import math
a,b,c = map(float, input().split())

delta = (b*b) - 4*a*c
if delta < 0:
    print('Impossivel calcular')
elif a == 0:
    print('Impossivel calcular')
else:
    x1 = ((b*-1) + math.sqrt(delta))/(2*a)
    x2 = ((b*-1) - math.sqrt(delta))/(2*a)
    print('R1 = {:.5f}'.format(x1))
>>>>>>> a
    print('R2 = {:.5f}'.format(x2))