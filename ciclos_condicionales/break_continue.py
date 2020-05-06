# Uso de palabras reservadas

titulo = "Curso de Python 3 - DR"

# Avanza a la siguiente Iteración
for caracter in titulo:
    if caracter == "P":
        continue
    print(caracter)

# Rompe el ciclo normal
for caracter in titulo:
    if caracter == "P":
        break
    print(caracter)
