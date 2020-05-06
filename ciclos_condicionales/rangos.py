# Manejo de Rangos

# un rango de números
for value in range(10):
    print(value)

# Un rango de números "Desde" "Hasta" con "salto"
for value in range(1,20,1):
    print(value)

# lista Iterable
lista = [1,2,3,4,5,6,7,8,9,10]

# Con "len"
for indice in range(len(lista)):
    print("Indice:", indice, "Valor:", lista[indice])

# Con "enumerate"
for indice, valor in enumerate(lista):
    print("Indice:", indice, "Valor:", valor)

# Con "enumerate" - demo Índice
for indice, valor in enumerate(lista, 10):
    print("Indice:", indice, "Valor:", valor)
