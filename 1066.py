'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''

par =  impar = pos = neg = 0
for i in range(5):
    x = int(input())
    if x%2 == 0:
        par +=1
    elif x%2 != 0:
        impar +=1

    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1

print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(pos,"valor(es) positivo(s)")
print(neg,"valor(es) negativo(s)")