# Listas
"""
7.2.1. Eliminar el último elemento de la lista
Método: pop()
Retorna: el elemento eliminado.

7.2.2. Eliminar un elemento por su índice
Método: pop(índice)
Retorna: el elemento eliminado.


7.2.3. Eliminar un elemento por su valor
Método: remove("valor")

"""

lista = ["uno" , "dos", "tres", "dos", "cuatro"]
print("Lista Original", lista)

respuesta = lista.pop()
print(respuesta)
print(lista)

respuesta = lista.pop(2)
print(respuesta)
print(lista)

lista.remove("dos")
print(lista)
