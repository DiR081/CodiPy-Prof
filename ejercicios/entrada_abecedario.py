"""
    Desarrollo ejercicio
  Remplazar cada letra de una frase dada por el usuario por la posición que le
  corresponde en el abecedario y mostrar el nuevo string en pantalla.
  (Los espacios no se remplazan) .
    Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
"""

# Diro81
# 6 May 2020
# leras, posición en el alfabeto

alfabeto = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w':23, 'x': 24, 'y': 25, 'z': 26
}

texto_usuario = input("Ingresa una frase:\n")

texto_minusculas = texto_usuario.lower()
texto_salida = ""

for letra in texto_minusculas:
    if letra in alfabeto:
        #print(alfabeto[letra])
        texto_salida = texto_salida + str(alfabeto[letra])
    else:
        texto_salida = texto_salida + letra

print("Tu frase:", texto_usuario)
print("La Salida:",texto_salida)
