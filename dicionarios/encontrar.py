"""  Dicionarios """

# Dicionario nuevo - No permite llaves repetidas
dicionario = {"a":1 , "b":2 , "c":3 , "a":4}

# Trae el valor
resultado = dicionario["a"]
print(resultado)

# No encontrado - genera Error
#resultado = dicionario["z"]
print(resultado)

# Encontrado - Sin Error
resultado = dicionario.get("Y")
print(resultado)

# Encontrado - Sin Error
resultado = dicionario.get("Y", "Respuesta sin Error")
print(resultado)

# Encontrado - Sin Error
resultado = dicionario.get("Y", {})
print(resultado)

# asigna y retorna el valor
# Encontrado - Sin Error
resultado = dicionario.setdefault("Z", {})
print(resultado)
resultado = dicionario.setdefault("a", {})
print(resultado)

# Usar la palabra reservada "in"
resultado = "x" in dicionario
print(resultado)
