'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

lista = []
for i in range(100):
    lista.append(int(input()))

a  = max(lista)
print(a)
print(lista.index(a)+1)