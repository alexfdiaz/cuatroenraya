def tableroVacio():
	return [
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0]
	]

def completarTableroEnOrden(secuencia, tablero):
	for indice, columna in enumerate(secuencia):
		fichaNumero = 1 + (indice % 2)
		soltarFichaEnColumna(fichaNumero, columna, tablero)
	return tablero


def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range(6, 0, -1):
		if tablero[fila - 1][columna - 1] == 0:
			tablero[fila - 1][columna - 1] = ficha
			return

def dibujarTablero(tablero):
	for fila in tablero:
		for celda in fila:
			if celda == 0:
				print('   ', end='')
			else:
				print(' %s ' % celda, end='')
		print('')

def secuenciaValida(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
			return False
	return True


secuencia = [1, 2, 3, 1, 3, 4, 8]
if secuenciaValida(secuencia):
	dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
else:
	print("Las columnas deberian ir de 1 a 7")