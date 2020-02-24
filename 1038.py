'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

1 - cachorro quente = R$4,00
2 - x - salada = R$4,50
3 - x - bacon = R$5,00
4 - torrada simples = R$2,00
5 - refrigerante = R$1,50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''

tabela = {
    1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5
}

cod, quant = map(int, input().split())

valor = tabela[cod] * quant
print('Total: R$ {:.2f}'.format(valor))