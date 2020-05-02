"""
    Manejo de Fechas
    Acividad:
        Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.
"""

# Importamos librerias
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

MENSAJE = """ Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario. """

# Se utiliza una función con un formato mas amigable
def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage


# Imprimir actividad
print(MENSAJE)

# Día actual
hoy = date.today()

# Fecha actual
now = datetime.now()

# La Hora
hora_tiempo = time.hour

# Imprimimos
print("Hoy es", hoy)
print("Ahora es", now)
#print("La Hora", hora_tiempo)

# Validador
#dt = datetime.date(2010, 6, 16)

# wk = now.isocalendar()[1]
# print("Hoy es la Semana",wk)


# Nueva Fecha manualmente
new_date = datetime(2020, 12, 31, 10, 15, 00, 00000)
print("Mi Nueva Fecha es", new_date)
# Mi nueva fecha en un formato definido en la funcion
print(current_date_format(new_date))


#Date
print("El día actual es {}".format(hoy.day))
print("El mes actual es {}".format(hoy.month))
print("El año actual es {}".format(hoy.year))


#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

#
print("Cuando nacistes?")
fecha_nacimiento_anno = int(input("Año:\n"))
fecha_nacimiento_mes = int(input("Mes:\n"))
fecha_nacimiento_dia = int(input("Día:\n"))

# Imprimimos
print()
print(fecha_nacimiento_anno)
print(fecha_nacimiento_mes)
print(fecha_nacimiento_dia)

fecha_nacimiento = datetime(fecha_nacimiento_anno, fecha_nacimiento_mes, fecha_nacimiento_dia, 1, 0, 00, 0000)
resto_dias_fechas = now - fecha_nacimiento

print("El número de días de vida es",resto_dias_fechas)

# Uso el IsoCalendar de python y optengo las semanas
#wk = dt.isocalendar()[1]
wk_fecha_actual = now.isocalendar()[1]
anno_fecha_actual = now.isocalendar()[0]
wk_fecha_nacimiento = fecha_nacimiento.isocalendar()[1]
anno_fecha_nacimiento = fecha_nacimiento.isocalendar()[0]
wk_por_anno = new_date.isocalendar()[1]
print("Año Actual",anno_fecha_actual)
print("Wk Actual",wk_fecha_actual)
print("Año Nacimiento",anno_fecha_nacimiento)
print("Wk Nacimiento",wk_fecha_nacimiento)
print("Wk en el 2020",wk_por_anno)


#Para los bisiestos averiguar cuales son bisiestos
anno = anno_fecha_nacimiento
total_anno_bisiestos = 0
anno_nacimiento_bisiesto = False
total_anno_vida = 0
while anno < anno_fecha_actual:
  #print(anno)
  if anno == anno_fecha_nacimiento:
      # Construyo el año a evaliuar
      new_date = datetime(anno, 12, 31, 10, 15, 00, 00000)
      wk_por_anno = new_date.isocalendar()[1]
      if wk_por_anno > 52:
          total_anno_bisiestos += 1
          if  anno == anno_fecha_nacimiento:
              anno_nacimiento_bisiesto = True
  # Aumento el apuntador
  anno += 1
  total_anno_vida += 1

# Resultados
print(total_anno_vida, total_anno_bisiestos, anno_nacimiento_bisiesto)

#print(semanas_edad)
