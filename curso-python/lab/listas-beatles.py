#  LABORATORIO

# Tiempo estimado

# 10-15 minutos
# Nivel de dificultad

# Fácil
# Objetivos

# Familiarizar al estudiante con:

#     Crear y modificar listas simples.
#     Utilizar métodos para modificar listas.

# Escenario

# Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

# La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).

# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

#     Paso 1: Crea una lista vacía llamada beatles.
#     Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
#     Paso 3: Emplea el ciclofor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
#     Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
#     Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.

# Por cierto, ¿eres fan de los Beatles?

# Paso 1:
Beatles = []
print("Paso 1:", Beatles)

# Paso 2:

Beatles.append ("John Lennon")
Beatles.append ("Paul McCartney")
Beatles.append ("George Harrison")
print("Paso 2:", Beatles)

# Paso 3:
for miembros in range(2):
    Beatles.append (input ("Nuevo miembro de la banda:"))
print("Paso 3:", Beatles)

# Paso 4:
del Beatles [-1]
del Beatles [-1]
print("Paso 4:", Beatles)

# Paso 5:
Beatles.insert (0, "RingoStarr")
print("Paso 5:", Beatles)
print("Los Fab:", len (Beatles))