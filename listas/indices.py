# Indices en Listas
"""
Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.

[:] Todos los elementos.
[start:] Todos los elementos desde el índice establecido(start).
[:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
[start:end] Todos los elementos de un rango de índices.
[start:end:step] Todos los elementos de un rango de índices con saltos.

"""

cursos = ["python" , "c" , "c++" , "c#" , "php" , "java", "flash"]

curso = cursos[4]
print(curso)

inv = cursos[::-1]
print(inv)
