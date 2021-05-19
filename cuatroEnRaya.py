def tableroVacio():
	return [
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0]
	]

def contenidoColumna(nro_columna, tablero):
	columna = []
	for fila in tablero:
		celda = fila[nro_columna - 1]
		columna.append(celda)
	return columna

def contenidoFila(nro_fila, tablero):
	return tablero[nro_fila - 1]

def columnas(tablero):
	listaDeColumnas = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0]
	]

	i = 0
	j = 0
	for fila in tablero:
		for celda in fila:
			listaDeColumnas[j][i] = celda
			j += 1
		i += 1
		j = 0
	return listaDeColumnas

def filas(tablero):
	listaDeFilas = tablero
	return listaDeFilas

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
	for i in range(23):
		if i == 0: print('\t\t╔', end = '')
		elif i == 22: print('╗')
		else: print('═', end = '')
	for fila in tablero:
		print('\t\t║', end = '')
		for celda in fila:
			if celda == 0:
				print('   ', end='')
			else:
				print(' %s ' % celda, end='')
		print('║')
	for i in range(23):
		if i == 0: print('\t\t╚', end = '')
		elif i == 22: print('╝')
		else: print('═', end = '')

def secuenciaValida(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
			return False
	return True

secuencia = [1, 2, 3, 1, 3, 4, 7, 6]

tablero = []
if secuenciaValida(secuencia):
	tablero = completarTableroEnOrden(secuencia, tableroVacio())
	dibujarTablero(tablero)
else:
	print("Las columnas deberian ir de 1 a 7")

'''print("Contenido de una columna")
print(contenidoColumna(1, tablero))

print("Contenido de una fila")
print(contenidoFila(6, tablero))

print("Listado de columnas")
print(columnas(tablero))

print("Listado de filas")
print(filas(tablero))'''