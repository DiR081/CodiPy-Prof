# Dicionarios - Eliminar Llaves y Valores

dicionario = {"g": 1, "b": 2, "c": 3, "d": 4, "e": 5 , "f": 6, "a": 7, "h": 8}

# Imprimir
print(len(dicionario))
print(dicionario)

# un del sensillo
del dicionario["g"]
# Imprimir
print(len(dicionario))
print(dicionario)

# Con el metod pop , con o sin retorno
valor_eliminado = dicionario.pop("h")
# Imprimir
print(valor_eliminado)
print(len(dicionario))
print(dicionario)

# Un dicionario vacio
dicionario = {}
# Imprimir
print(len(dicionario))
print(dicionario)

# Un metodo
dicionario.clear()
# Imprimir
print(len(dicionario))
print(dicionario)
