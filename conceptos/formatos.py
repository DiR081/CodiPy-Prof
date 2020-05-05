# Manejo de Texto

texto = "   curso de Python 3  "

# texto Primera Letra a Mayusculas
resultado = texto.capitalize()
print(resultado)

# texto en modo Titulo
resultado = texto.title()
print(resultado)

# Invierte Mayus / Minus
resultado = texto.swapcase()
print(resultado)

# cadena a Minusculas
resultado = texto.lower()
print(resultado)

# cadena a Mayusculas
resultado = texto.upper()
print(resultado)

# Validar ttexto en Mayusculas o Minusculas
print(resultado.isupper())
print(resultado.islower())

# Reemplazo  X -> Y -> nVeces
resultado = texto.replace("Python", "Ruby", 1)
print(resultado)

# Elimina los espacion Iniciales y finales de la cadena
resultado = texto.strip()
print(resultado)


########################################################3

curso = "Python"
version = "3"

# Utilización metodo %
resultado = "Curso de %s %s" %(curso, version)
print(resultado)

# Utilización modo format
resultado = "Curso de {} {}".format(curso, version)
print(resultado)

# Utilización modo format con nombre
resultado = "Curso de {a} {b}".format(b=version, a=curso)
print(resultado)

# Concatenación
curso = "Curso de Python"

# Se crea un nuevo string con el remplazo y la utilidad de Concatenación
curso = "c" + curso[1:] + " " + str(3) + " en código facilito."

print(curso)
