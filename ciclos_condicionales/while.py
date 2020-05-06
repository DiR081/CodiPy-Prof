#

numero = 123567890
contador = 0

while numero > 1:
    contador += 1
    numero = numero / 10
else:
    print("Cantidad de digitos %s" %contador)
