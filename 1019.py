tempo = int(input())

segundos = minuto = houra = 0

if tempo >= 3600:
	houra += tempo//3600

resto = tempo - (3600*houra)

if resto >= 60:
	minuto += resto//60

resto = resto - (60*minuto)
segundos += resto

print("{}:{}:{}".format(houra,minuto,segundos))
