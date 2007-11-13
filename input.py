from sdes import *

def binar(d):
	"""devuelve un string de 8 "bits" cuando recibe un entero"""
        s=''
        t={'0':'000','1':'001','2':'010','3':'011',
       '4':'100','5':'101','6':'110','7':'111'}
        for c in oct(d)[1:]:
            s+=t[c]
	
	#completa a 8 bits
	if len(s) < 8:
		for i in range(8 - len(s)):
			s = '0' + s
	#convierte a entero
	s = [int(bit) for bit in s]
	return s[-8:]


if __name__ == '__main__':
	entrada = raw_input('Ingrese la cadena a codificar:\n')
	while 1:
		clave = raw_input('Ingrese su clave, en formato binario de 10 bits')
		if len(clave)==10:
			try:
				int(clave,2)
			except:
				continue
			break
	#clave = '1010101010'
	clave = [int(i) for i in clave]
	sal = []
	for char in entrada:
		print "********** plano = " + str(binar(ord(char)))
		char = sdes(binar(ord(char)), clave)
		sal.append(char)		

	print "SALIDA: " + repr(sal)
	