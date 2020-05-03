# Operadores comunes

lista = [8.17, 90, 2, 5, 44, 1, 1.32]

# Ordena de Menoar a Mayor
lista.sort()
menor = lista[0]

# Ordenar de Mayor a Menor
lista.sort(reverse=True)
mayor = lista[0]

# Menor
menor = min(lista)

# Mayor
mayor = max(lista)

# Largo
longuitud = len(lista)

# Averiguar Si X valor está en la lista
en_lista = 8.17 in lista
if en_lista:
    indice = lista.index(8.17)
    print("indice", indice)

# Contar la N cantidad de veces que está un valor
cantidad = lista.count(1)
print("Cuantas veces", cantidad)

# Imprimir
print(lista)
