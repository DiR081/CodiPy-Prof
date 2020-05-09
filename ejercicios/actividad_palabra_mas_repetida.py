"""
    Actividad - Link
        https://codigofacilito.com/articulos/ejercicios_conceptos_basicos_python

        Mostrar en pantalla la palabra que más se repita junto con la cantidad
         de veces que lo hace del capituló número uno de Frankenstein
         http://umich.edu/~umfandsf/other/ebooks/frank10.txt

"""

# Diro81
# 8 May 2020
# leras, posición en el alfabeto


MENSAJE = """  Mostrar en pantalla la palabra que más se repita junto con la cantidad
  de veces que lo hace del capituló número uno de Frankenstein. """

alfabeto = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w':23, 'x': 24, 'y': 25, 'z': 26
}

# List desde un rango de números 0-9 como string
numeros= []
for value in range(10):
    numeros.append(str(value))

# Imprimimos
print("")
print(MENSAJE)
print(".")
print("")
print(".")


#
# Eliminar los apostrofes puede no ser necesario
# Eliminar los signos de puntuación y caracteres especiales
# Poner todo en un solo formato May/Min
#

# Abrir el archivo y veamos que signos hay
archivo = open("frank10.txt", 'r')
datos_texto = archivo.read() # datos_texto es un string
archivo.close()

# Imprimimos
print("Lo que el puntero archivo es: %s" %archivo)
print("El tipo de dato que es datos texto:",type(datos_texto))
print("Hay un total de %s caracteres." %int(len(datos_texto)))

# todo a minusculas
datos_texto_mins = datos_texto.lower()

# Eliminarmos cualquier cosa que no este en el dic alfabeto
datos_texto_mins_alf = ""
signos_no_alf = ""
for letra in datos_texto_mins:
    if letra in alfabeto or letra == " " or letra == "\n" or letra in numeros:
        letra = " " if letra == "\n" else letra
        # Concatena el sttring sin sin signos
        datos_texto_mins_alf = datos_texto_mins_alf + letra
    else:
        signos_no_alf = signos_no_alf + letra

# Lista sin saltos de linea, string y solo palabras
palabras_list = datos_texto.splitlines()
datos_texto = " ".join(palabras_list)
palabras_list = datos_texto.split()

palabras_texto = datos_texto_mins_alf.split()

print("Hay %s Palabras." %str(len(palabras_list)))
print("Hay %s Palabras." %str(len(palabras_texto)))

# Imprimir ayuda Grafica
# cont = 0
# while cont <= 40:
#     print("")
#     print(palabras_list[cont])
#     print(palabras_texto[cont])
#     cont += 1

# Dicionario nuevo - Llave / Valor
cont_a = 0
dic_total_por_palabra = {}
#for palabra in palabras_texto:
for cont_b in range(len(palabras_texto)):
    # Cuento Cuantas veces está cada palabra
    palabra = palabras_texto[cont_b]
    #print(palabra)
    cont_a = palabras_texto.count(palabra)
    dic_total_por_palabra[palabra] = cont_a
    # Elimina el Elemento de la lista --- :( solo elimina la primera ocurrencia
    #palabras_texto = palabras_texto.remove(palabra)

print("El total de palabras fueron %s" %len(dic_total_por_palabra))
# # llaves del diccionario
# resultado_obj = dic_total_por_palabra.keys()
# # transformado a lista o tupla
# resultado = list(resultado_obj)
# print(resultado)

# # En modo objeto - parametro del diccionario
# resultado_obj = dic_total_por_palabra.items()
# # transformado a lista o tupla
# resultado = list(resultado_obj)
# # Imprimir
# print(resultado)

# En modo objeto - parametro del diccionario
resultado_obj = dic_total_por_palabra.keys()
# transformado a lista o tupla
resultado_llaves = list(resultado_obj)
# Imprimir
#print(resultado)

# En modo objeto - parametro del diccionario
resultado_obj = dic_total_por_palabra.values()
# transformado a lista o tupla
resultado_valores = list(resultado_obj)
# Imprimir
#print(resultado)

mas_veces_valor = max(resultado_valores)
indice_palabra_mas = resultado_valores.index(mas_veces_valor)

palabra_mas_repetida = resultado_llaves[indice_palabra_mas]

# Imprimir
print("La palabra más repetida es:")
print(palabra_mas_repetida)
