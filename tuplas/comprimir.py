# Manejo Tuplas

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
lista = [1, 20, 30, 40]
tupla_dos = [100, 200, 300]

# Se crea el Objeto encapsulado

resultado = zip(tupla, lista, tupla_dos)
print(resultado)

resultado = tuple(resultado)
print(resultado)

# Se optienen los valores gracias a los comodines * y _
primero, segundo, *_, ultimo = tupla
