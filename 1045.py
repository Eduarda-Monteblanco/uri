<<<<<<< HEAD
'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO

se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''
valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

lista = [a,b,c]
lista.sort(reverse=True)

if lista[0] >= (lista[1]+lista[2]):
    print('NAO FORMA TRIANGULO')
else:
    if lista[0]**2 == ((lista[1]**2)+(lista[2]**2)):
        print('TRIANGULO RETANGULO')
    if lista[0]**2 > ((lista[1]**2)+(lista[2]**2)):
        print('TRIANGULO OBTUSANGULO')
    if lista[0]**2 < ((lista[1]**2)+(lista[2]**2)):
        print('TRIANGULO ACUTANGULO')
    if lista[0] == lista[1] and lista[1] == lista[2]:
        print('TRIANGULO EQUILATERO')
    elif lista[0] == lista[1] or lista[1] == lista[2] or lista[2] == lista[0]:
        print('TRIANGULO ISOSCELES')

=======
'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO

se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''
valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

lista = [a,b,c]
lista.sort(reverse=True)

if lista[0] >= (lista[1]+lista[2]):
    print('NAO FORMA TRIANGULO')
else:
    if lista[0]**2 == ((lista[1]**2)+(lista[2]**2)):
        print('TRIANGULO RETANGULO')
    if lista[0]**2 > ((lista[1]**2)+(lista[2]**2)):
        print('TRIANGULO OBTUSANGULO')
    if lista[0]**2 < ((lista[1]**2)+(lista[2]**2)):
        print('TRIANGULO ACUTANGULO')
    if lista[0] == lista[1] and lista[1] == lista[2]:
        print('TRIANGULO EQUILATERO')
    elif lista[0] == lista[1] or lista[1] == lista[2] or lista[2] == lista[0]:
        print('TRIANGULO ISOSCELES')

>>>>>>> a
