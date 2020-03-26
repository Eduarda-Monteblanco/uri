'''
Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.

Entrada
O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 ≤ M ≤ 20) e N (0 ≤ N ≤ 20). O fim da entrada é determinado por eof.

Saída
Para cada caso de teste de entrada, seu programa deve imprimir uma única linha, contendo um número que é a soma de ambos os fatoriais (de M e N).
'''
def main(n):
    fat = 1
    i = 2
    while i <= n:
        fat *= i
        i += 1
    return fat

while True:
    try:
        soma = 0
        n,m = map(int,input().split())
        x = main(n)
        soma += x
        y = main(m)
        soma += y
        print(soma)
    except EOFError:
        break

    

