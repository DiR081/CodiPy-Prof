# Metodos y Herramientas para los strings

texto = "En el siguiente texto tenemos varias palabras, para hacer las pruebas."

# Con el metodo contar
resultado = texto.count("texto")
print(resultado)

# Uso de la palabra reservada "in"
resultado = "texto" in texto
print(resultado)

# Uso de la metodo encontrar
resultado = texto.find("texto")
sub = texto[resultado : resultado + len("texto")]
print(resultado)
print(sub)

# metodo para el inicio o fin de la cadena
resultado = texto.startswith("El")
print(resultado)

resultado = texto.endswith("pruebas.")
print(resultado)
