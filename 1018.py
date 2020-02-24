<<<<<<< HEAD
cem = cinquenta = vinte = dez = cinco = dois = um = 0

valor = int(input())

if valor >= 100:
	cem += valor//100
resto = valor - (100*cem)

if resto < 100 and resto >=50: 
	cinquenta += resto//50
resto = resto - (50*cinquenta)

if resto < 50 and resto >=20: 
	vinte += resto//20
resto = resto - (20*vinte)

if resto < 20 and resto >=10: 
	dez += resto//10
resto = resto - (10*dez)

if resto < 10 and resto >=5: 
	cinco += resto//5
resto = resto - (5*cinco)

if resto < 5 and resto >=2: 
	dois += resto//2
resto = resto - (2*dois)

if resto < 2 and resto >=1: 
	um += resto//1
resto = resto - (2*um)

print(valor)
print(cem, "nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez,"nota(s) de R$ 10,00")
print(cinco,"nota(s) de R$ 5,00")
print(dois,"nota(s) de R$ 2,00")
=======
cem = cinquenta = vinte = dez = cinco = dois = um = 0

valor = int(input())

if valor >= 100:
	cem += valor//100
resto = valor - (100*cem)

if resto < 100 and resto >=50: 
	cinquenta += resto//50
resto = resto - (50*cinquenta)

if resto < 50 and resto >=20: 
	vinte += resto//20
resto = resto - (20*vinte)

if resto < 20 and resto >=10: 
	dez += resto//10
resto = resto - (10*dez)

if resto < 10 and resto >=5: 
	cinco += resto//5
resto = resto - (5*cinco)

if resto < 5 and resto >=2: 
	dois += resto//2
resto = resto - (2*dois)

if resto < 2 and resto >=1: 
	um += resto//1
resto = resto - (2*um)

print(valor)
print(cem, "nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez,"nota(s) de R$ 10,00")
print(cinco,"nota(s) de R$ 5,00")
print(dois,"nota(s) de R$ 2,00")
>>>>>>> a
print(um, "nota(s) de R$ 1,00")