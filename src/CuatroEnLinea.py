def tableroVacio():
	return [[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			]

def soltarFichaEnColumna(ficha,columna,tablero):
	for fila in range(6,0,-1):
		if tablero[fila - 1][columna - 1] == 0:
			tablero[fila - 1][columna - 1] = ficha
			return

def completarTableroEnOrden(secuencia, tablero):
	x = 0
	for i in secuencia:
		if x % 2 == 0:
			soltarFichaEnColumna(1,i,tablero)
			x += 1
		else:
			soltarFichaEnColumna(2,i,tablero)
			x += 1
	return tablero

def dibujarTablero(tablero):
	for fila in tablero:
		print('|', end = " ")
		for celda in fila:
			if celda == 0:
				print(" 0 ", end = ' ')
			else:
				print(" %s " % celda, end = ' ')
		print('|')
	print('+-----------------------------+')

def columnaValida(secuencia):
    for x in secuencia:
        if x > 7 or x < 1:
            return False
    return True

def contenidoColumna(nroCol, tablero):
	columna = []
	for fila in tablero:
		celda = fila[nroCol - 1]
		columna.append(celda)
	return columna

def contenidoFila(nroFil, tablero):
	fila = tablero[nroFil-1]     
	return fila 

def Columnas(tablero):
	columnas=[]
	for x in range(7,0,-1):
		columnas.append(contenidoColumna(x,tablero)) #Esta función muestra las columnas de derecha a izquierda
	return columnas

def Filas(tablero):
	filas=[]
	for x in range(6,0,-1):
		filas.append(contenidoFila(x,tablero)) #Esta función muestra las filas de abajo para arriba
	return filas


secuencia = [1, 2, 6, 2, 5, 4, 2]
if columnaValida(secuencia) == False:
	print("\nSecuencia de soltado de ficha en columna no valida")
else:
	tablero = completarTableroEnOrden(secuencia, tableroVacio())
	dibujarTablero(tablero)

