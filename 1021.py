<<<<<<< HEAD
valor = float(input())
cem = valor // 100
valor = valor - cem*100

cinquenta = valor // 50
valor = valor - cinquenta*50

vinte = valor // 20
valor = valor - vinte*20

dez = valor // 10
valor = valor - dez*10

cinco = valor // 5
valor = valor - cinco*5

dois = valor // 2
valor = valor - dois*2

um = valor // 1
valor = valor - um*1
um = float('%.2f'% um)
valor = float('%.2f'% valor)

cinquenta_cent = valor // 0.5
valor = valor - cinquenta_cent*0.5
cinquenta_cent = float('%.2f'% cinquenta_cent)
valor = float('%.2f'% valor)

vinte_e_cinco_cent = valor // 0.25
valor = valor - vinte_e_cinco_cent*0.25
vinte_e_cinco_cent = float('%.2f'% vinte_e_cinco_cent)
valor = float('%.2f'% valor)

dez_cent = valor // 0.10
valor = valor - dez_cent*0.10
dez_cent = float('%.2f'% dez_cent)
valor = float('%.2f'% valor)

cinco_cent = valor // 0.05
valor = valor - cinco_cent*0.05
cinco_cent = float('%.2f'% cinco_cent)
valor = float('%.2f'% valor)

um_cent = valor * 100
um_cent = float('%.2f'% um_cent)
valor = float('%.2f'% valor)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int(dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(cinquenta_cent)))
print('{} moeda(s) de R$ 0.25'.format(int(vinte_e_cinco_cent)))
print('{} moeda(s) de R$ 0.10'.format(int(dez_cent)))
print('{} moeda(s) de R$ 0.05'.format(int(cinco_cent)))
=======
valor = float(input())
cem = valor // 100
valor = valor - cem*100

cinquenta = valor // 50
valor = valor - cinquenta*50

vinte = valor // 20
valor = valor - vinte*20

dez = valor // 10
valor = valor - dez*10

cinco = valor // 5
valor = valor - cinco*5

dois = valor // 2
valor = valor - dois*2

um = valor // 1
valor = valor - um*1
um = float('%.2f'% um)
valor = float('%.2f'% valor)

cinquenta_cent = valor // 0.5
valor = valor - cinquenta_cent*0.5
cinquenta_cent = float('%.2f'% cinquenta_cent)
valor = float('%.2f'% valor)

vinte_e_cinco_cent = valor // 0.25
valor = valor - vinte_e_cinco_cent*0.25
vinte_e_cinco_cent = float('%.2f'% vinte_e_cinco_cent)
valor = float('%.2f'% valor)

dez_cent = valor // 0.10
valor = valor - dez_cent*0.10
dez_cent = float('%.2f'% dez_cent)
valor = float('%.2f'% valor)

cinco_cent = valor // 0.05
valor = valor - cinco_cent*0.05
cinco_cent = float('%.2f'% cinco_cent)
valor = float('%.2f'% valor)

um_cent = valor * 100
um_cent = float('%.2f'% um_cent)
valor = float('%.2f'% valor)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int(dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(cinquenta_cent)))
print('{} moeda(s) de R$ 0.25'.format(int(vinte_e_cinco_cent)))
print('{} moeda(s) de R$ 0.10'.format(int(dez_cent)))
print('{} moeda(s) de R$ 0.05'.format(int(cinco_cent)))
>>>>>>> a
print('{} moeda(s) de R$ 0.01'.format(int(um_cent)))