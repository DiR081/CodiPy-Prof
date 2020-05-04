# Manejo Separador y Uniones

# string
lenguajes = "java; Python; Ruby; C; C++; C#; Perl; Swift; PHP"

# string texto
texto = """ Este es
un

texto con
saltos"""

# Un string
separador = "; "  # " " (espacio) es por defecto

# Divide el string en parte como una lista según separador
resultado = lenguajes.split(separador)  # resultado es ahora una lista

# Une una lista, con algo en este caso con el separador original
nueva_lista = separador.join(resultado)

# divide el texto
otra_lista = texto.splitlines()

# Imprimir
print(lenguajes)
print(resultado)
print(nueva_lista)
print(otra_lista)
