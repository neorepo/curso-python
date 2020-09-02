#Ejemplo 1
# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

#Ejemplo 2
# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# 0 termina la ejecución
while numero != 0: # while numero != 0: = while numero:
    # verificar si el número es impar
    if numero % 2 == 1: # if numero % 2 == 1: = if numero % 2:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
        # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)

