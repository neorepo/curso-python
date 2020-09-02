def irACaminar():
    print ('Estamos caminado')

def irAlCine():
    print ('Vamos al cine')

def almorzar():
    print ('Almorzandooo!')
    
# emperador1833@gmail.com
# Crimson3381
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Datos de entrada
# hora = 12
# min = 17
# dura = 59
# resultado esperado: 13:16

# hora = 23
# min = 58
# dura = 642
# resultado esperado: 10:40

# hora = 0
# min = 1
# dura = 2939
# resultado esperado: 1:0

hora = ( ( (hora * 60) + min + dura ) // 60 ) % 24
min = ( min + dura ) % 60

print(hora, min, sep=":")
nombre = "Julio"
print(0.0000000000000000000001)

climaEsBueno = True

if climaEsBueno:
    irACaminar()
else:
    irAlCine()
almorzar()


#lee dos números
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)
