# Entrada datos desde Consola

# Pregunta para interactuar
print("Cúal es tu nombre?")
# Siempre entra es de tipo String
nombre = input()

print("Cúal es tu edad?")
# Se formatea la cadena a un número Entero
edad = int(input())

# Imprime y recive entrada
peso = float(input("Cúal es tu peso?"))

# + ajuste - Salto de línea y validación Boleana
autorizado = input("¿Autorizado?(S/N)\n") == "S"

# Imprime
print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)
