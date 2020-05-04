# Manejo de Listas y tuplas

lista = ["Yo", "Soy", "Una", "Lista", "Originalmente"]
tupla = ()"Yo", "Soy", "Una", "Tupla", "Originalmente")

mensaje = "Yo soy un mensaje."

nueva_lista = list(tupla)
nueva_tupla = tuple(lista)

otra_lista = list(mensaje)
otra_tupla = tuple(mensaje)

# Imprimir
print(nueva_tupla)
print(otra_lista)
