# LABORATORIO

# Tiempo estimado

# 15-20 minutos
# Nivel de dificultad

# Fácil
# Objetivos

#     Mejorar la habilidad de implementar números, operadores y operaciones aritméticas en Python.
#     Utilizar la función print() y sus capacidades de formateo.
#     Aprender a expresar fenómenos del día a día en términos de un lenguaje de programación.

# Escenario

# La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado debe ser mostrado en la consola.

# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

# No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

# Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.
# Datos de Prueba

# Entrada de muestra:
# 12
# 17
# 59

# Salida esperada: 13:16

# Entrada de muestra:
# 23
# 58
# 642

# Salida esperada: 10:40

# Entrada de muestra:
# 0
# 1
# 2939

# Salida esperada: 1:0

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
min = min + dura # encuentra el total de minutos
hora = hora + min // 60 # encuentra el número de horas ocultos en los minutos y actualiza las horas
min = min % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23)
print(hora, ":", min, sep='')