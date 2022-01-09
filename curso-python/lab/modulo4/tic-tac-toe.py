# PROYECTO

# Tiempo estimado
# 30-60 minutos

# Nivel de dificultad
# Medio/difícil

# Objetivos
# Perfeccionar las habilidades del estudiante al emplear Python para resolver problemas complejos.
# La integración de técnicas de programación en un solo programa consistente de varias partes.
# Escenario
# Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, Hemos decidido simplificar el juego. Aquí están nuestras reglas:

# La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
# El usuario (por ejemplo, tu) jugará utilizando las 'O's.
# El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
# Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
# El usuario ingresa su movimiento introduciendo el numero de cuadro elegido. El numero debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
# El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
# La maquina responde con su movimiento y se verifica el estado del juego.
# No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
# El ejemplo del programa es el siguiente:

# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Ingresa tu movimiento: 1
# +-------+-------+-------+
# |       |       |       |
# |   O   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Ingresa tu movimiento: 8
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Ingresa tu movimiento: 4
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Ingresa tu movimiento: 7
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# ¡Has Ganado!

# Requerimientos
# Implementa las siguientes características:

# El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

# board[fila][columna]


# Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre).
# La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
# Implementa las funciones definidas para ti en el editor.

# Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

# Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

# from random import randrange

# for i in range(10):
#     print(randrange(8))

from random import randrange

def DisplayBoard(board):
	print("+-------" * 3,"+",sep="")
	for row in range(3):
		print("|       " * 3,"|",sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def EnterMove(board):
	ok = False	# suposición falsa - lo necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. Ingrésalo nuevamente.
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X'] 
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Campo ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado

def MakeListOfFreeFields(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # itera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free


def VictoryFor(board,sgn):
	if sgn == "X":	# ¿Estamos buscando X?
		who = 'yo'	# Si, es la maquina
	elif sgn == "O": # ... o estamos buscando O?
		who = 'tu'	# Si, es el usuario
	else:
		who = None	# ¡No debemos de caer aquí!
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# revisar filas rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # revisar columnas rc
			return who
		if board[rc][rc] != sgn: # revisar la primer diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def DrawMove(board):
	free = MakeListOfFreeFields(board) # hace una lista de los cuadros vacios o libres
	cnt = len(free)
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla 
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = MakeListOfFreeFields(board)
humanturn = True # ¿De quien es turno ahora?
while len(free):
	DisplayBoard(board)
	if humanturn:
		EnterMove(board)
		victor = VictoryFor(board,'O')
	else:	
		DrawMove(board)
		victor = VictoryFor(board,'X')
	if victor != None:
		break
	humanturn = not humanturn		
	free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victor == 'tu':
	print("¡Has ganado!")
elif victor == 'yo':
	print("¡He ganado!")
else:
	print("¡Empate!")