'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	                    Percentual de Reajuste
0 - 400.00                  15%
400.01 - 800.00             12%
800.01 - 1200.00            10%
1200.01 - 2000.00           7%
Acima de 2000.00            4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
'''
salario = float(input(''))

if salario <= 400.00:
    reajuste = salario*0.15
    per = 15
    salario = salario+reajuste
elif salario > 400.00 and salario <= 800.00:
    reajuste = salario*0.12
    per = 12
    salario = salario+reajuste

elif salario > 800.00 and salario <= 1200.00:
    reajuste = salario*0.1
    per = 10
    salario = salario+reajuste

elif salario > 1200.00 and salario <= 2000.00:
    reajuste = salario*0.07
    per = 7
    salario = salario+reajuste

elif salario > 2000.00:
    reajuste = salario*0.04
    per = 4
    salario = salario+reajuste


print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(per))
