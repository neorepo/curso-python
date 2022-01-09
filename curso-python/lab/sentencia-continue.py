# LABORATORIO

# Tiempo estimado

# 10-15 minutos
# Nivel de dificultad

# Fácil
# Objetivos

# Familiarizar al estudiante con:

#     Utilizar la instrucción continue en los ciclos.
#     Reflejar situaciones de la vida real en código de computadora.

# Escenario

# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las declaraciones dentro del ciclo.

# Se puede usar tanto con while y ciclos for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

#     Un ciclo for.
#     El concepto de ejecución condicional (if-elif-else).
#     La declaración continue.

# Tu programa debe:

#     Pedir al usuario que ingrese una palabra.
#     Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
#     Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
#     Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

# Prueba tu programa con los datos que le proporcionamos.

# Datos de prueba

# Entrada de muestra: Gregory

# Salida esperada:
# G
# R
# G
# R
# Y

# Entrada de muestra: abstemious

# Salida esperada:
# B
# S
# T
# M
# S

# Entrada de muestra: IOUEA

# Salida esperada:
 
userWord = input ("Ingresa tu palabra:")
userWord = userWord.upper ()

for letter in userWord:
   if letter == "A":
        continue
   elif letter == "E":
        continue
   elif letter == "I":
        continue
   elif letter == "O":
        continue
   elif letter == "U":
        continue
   else:
        print(letter)