"""
    Actividad - Link
        https://codigofacilito.com/articulos/ejercicios_conceptos_basicos_python

        Calcular el número de vueltas que da una llanta en 1 km,
        dado que el diámetro de la llanta es de 50 cm,
        mostrar el resultado en pantalla.

"""
#from math import Math

MENSAJE = """   Calcular el número de vueltas que da una llanta en 1 km,
        dado que el diámetro de la llanta es de 50 cm,
        mostrar el resultado en pantalla."""

# Imprimimos
print(MENSAJE)

PI = float(3.1416)
LARGO_PISTA = 1000 # En metros
DIAMETRO_RUEDA = float(0.50)  # en metros

# Formula Perimetro => C = 2 . Pi . r
perimetro = PI * DIAMETRO_RUEDA

# Calculo vueltas Dividiendo Longuitud Total en la de una vuelta de la rueda
vueltas = LARGO_PISTA / perimetro

# Imprimimos
print("Perimetro", perimetro)
print("Total Vueltas", vueltas)
