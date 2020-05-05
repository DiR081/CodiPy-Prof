"""  Dicionarios """

# Dicionario nuevo - No permite llaves repetidas
dicionario = {"a":1 , "b":2 , "c":3 , "d":4 , "e":5 , "f":6 , "g":7}

# En modo objeto - parametro del diccionario
resultado_obj = dicionario.keys()
# transformado a lista o tupla
resultado = list(resultado_obj)
# Imprimir
print(resultado)

# En modo objeto - parametro del diccionario
resultado_obj = dicionario.values()
# transformado a lista o tupla
resultado = tuple(resultado_obj)
# Imprimir
print(resultado)

# En modo objeto - parametro del diccionario
resultado_obj = dicionario.items()
# transformado a lista o tupla
resultado = list(resultado_obj)
# Imprimir
print(resultado)
