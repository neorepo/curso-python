# LABORATORIO

# Tiempo estimado

# 5 minutos
# Nivel de dificultad

# Muy fácil
# Objetivos

# Familiarizar al estudiante con:

#     Usar instrucciones básicas relacionadas con listas.
#     Crear y modificar listas.

# Escenario

# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.

# Tu tarea es:

#     Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (paso 1).
#     Escribir una línea de código que elimine el último elemento de la lista (paso 2).
#     Escribir una línea de código que imprima la longitud de la lista existente (paso 3).

# ¿Listo para este desafío?

listaSombrero = [1, 2, 3, 4, 5]

# Paso 1
listaSombrero[2] = int (input("Ingrese un número entero:"))

# Paso 2
listaSombrero[-1]

# Paso 3
print(len(listaSombrero))