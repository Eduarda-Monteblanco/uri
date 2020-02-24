'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''

pos =  0
lista = []
media = 0
for i in range(6):
    lista.append(float(input('')))

for i in range(6):
    if lista[i] > 0:
        pos += 1
        media += lista[i]

print(pos,'valores positivos')
print('{:.1f}'.format(media/pos))