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
		for celda in fila:
			if celda == 0:
				print(" 0 ", end = ' ')
			else:
				print(" %s " % celda, end = ' ')
		print( )

def columnaValida(secuencia):
    for x in secuencia:
        if x > 7 or x < 1:
            return False
    return True

secuencia = [1, 2, 6, 2, 5, 4, 2]
if columnaValida(secuencia) == False:
	print("\nSecuencia de soltado de ficha en columna no valida")
else:
	dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))

