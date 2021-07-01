from src.CuatroEnLinea import contenidoFila

def test_contenido_columna():
	tablero = [[0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [2, 0, 0, 0, 0, 0, 0],
			   [1, 1, 2, 1, 2, 0, 0],
			]

	assert [2, 0, 0, 0, 0, 0, 0] == contenidoFila(5,tablero)