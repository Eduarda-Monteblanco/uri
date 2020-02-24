'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''
pos =  0
lista = []
for i in range(6):
    lista.append(float(input('')))

for i in range(6):
    if lista[i] > 0:
        pos += 1

print(pos,'valores positivos')