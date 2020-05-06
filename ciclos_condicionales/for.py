# el ciclo for

# Simple
numeros = [1,2,3,4,5,6,7,8,9,0]

for value in numeros:
    print(value)

# for en dicionario
dicionario = { "a":1 , "b":2, "c":3 }

for llave in dicionario:
    print(llave)

# varios valores
datos = ( (10 , 20) , ["Carros", "Casas"] , {"a":1, "b":2} )

# El objeto
for valor in datos:
    print(valor)

# Una variable a cada valor
for valor1, valor2 in datos:
    print(valor1, valor2)
