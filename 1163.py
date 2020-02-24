<<<<<<< HEAD
'''
Em uma terra distante existem duas cidades, a Nlogônia onde vivem os Nlogoneses, e Ducklogônia onde vivem seus vizinhos os Duckneses, já à algum tempo estas duas cidades estão em guerra e agora em uma tentativa de ganhar a guerra os Duckneses pretendem atacar a cidade da Nlogônia com um bodoque que atira patos, porem para que não haja erro eles pediram que você construa um programa que dados os valores da altura do bodoque (h), os pontos onde inicia (p1) e onde termina (p2) a cidade da Nlogônia, o ângulo do disparo ( α) e a velocidade do lançamento, calcule se o projetil atingira o alvo.

Para os cálculos assuma que a aceleração da gravidade é g = 9.80665 e que π = 3.14159.

Entrada
Existem vários casos de teste, cada caso inicia com 1 valor de ponto flutuante h (1 ≤ h ≤ 150) indicando a altura do bodoque, a próxima linha contem 2 valores inteiros p1 e p2 (1 ≤ p1, p2 ≤ 9999) indicando onde inicia e onde termina a Nlogônia, a linha seguinte contem um inteiro n (1 ≤ n ≤ 100) indicando o numero de tentativas que serão feitas para acertar a Nlogônia, as n linhas seguintes contem dois valores de ponto flutuante com os valores do ângulo α (1 ≤ α ≤ 180) e a velocidade V (1 ≤ V ≤ 150) do disparo.

O final do arquivo de entrada é determinado por EOF.

Saída
Para cada disparo, seu programa deve imprimir uma única linha no seguinte formato, “X -> DUCK” para quando o pato acertar a Nlogônia ou “X -> NUCK” quando o pato não acertar a Nlogônia, onde X eh a distancia máxima que o projetil atingiu até chegar ao chão (Y=0). X deve ser impresso com 5 casas decimais.
'''
import math
g = 9.80665
π = 3.14159

h = float(input())
p1,p2 = map(int,input().split())
n = int(input())

for i in range(n):
    angulo,v = map(float, input().split())
    angulo = angulo*2
    v = v**2
    a = (v*math.sin(angulo))/g

    if a >= p1 and a <= p2:
        print('{:.5f} -> DUCK'.format(a))
    else:
        print('{:.5f} -> NUCK'.format(a))
=======
'''
Em uma terra distante existem duas cidades, a Nlogônia onde vivem os Nlogoneses, e Ducklogônia onde vivem seus vizinhos os Duckneses, já à algum tempo estas duas cidades estão em guerra e agora em uma tentativa de ganhar a guerra os Duckneses pretendem atacar a cidade da Nlogônia com um bodoque que atira patos, porem para que não haja erro eles pediram que você construa um programa que dados os valores da altura do bodoque (h), os pontos onde inicia (p1) e onde termina (p2) a cidade da Nlogônia, o ângulo do disparo ( α) e a velocidade do lançamento, calcule se o projetil atingira o alvo.

Para os cálculos assuma que a aceleração da gravidade é g = 9.80665 e que π = 3.14159.

Entrada
Existem vários casos de teste, cada caso inicia com 1 valor de ponto flutuante h (1 ≤ h ≤ 150) indicando a altura do bodoque, a próxima linha contem 2 valores inteiros p1 e p2 (1 ≤ p1, p2 ≤ 9999) indicando onde inicia e onde termina a Nlogônia, a linha seguinte contem um inteiro n (1 ≤ n ≤ 100) indicando o numero de tentativas que serão feitas para acertar a Nlogônia, as n linhas seguintes contem dois valores de ponto flutuante com os valores do ângulo α (1 ≤ α ≤ 180) e a velocidade V (1 ≤ V ≤ 150) do disparo.

O final do arquivo de entrada é determinado por EOF.

Saída
Para cada disparo, seu programa deve imprimir uma única linha no seguinte formato, “X -> DUCK” para quando o pato acertar a Nlogônia ou “X -> NUCK” quando o pato não acertar a Nlogônia, onde X eh a distancia máxima que o projetil atingiu até chegar ao chão (Y=0). X deve ser impresso com 5 casas decimais.
'''
import math
g = 9.80665
π = 3.14159

h = float(input())
p1,p2 = map(int,input().split())
n = int(input())

for i in range(n):
    angulo,v = map(float, input().split())
    angulo = angulo*2
    v = v**2
    a = (v*math.sin(angulo))/g

    if a >= p1 and a <= p2:
        print('{:.5f} -> DUCK'.format(a))
    else:
        print('{:.5f} -> NUCK'.format(a))
>>>>>>> a
    