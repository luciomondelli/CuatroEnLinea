from src.CuatroEnLinea import contenidoColumna

def test_contenido_columna():
	tablero = [[0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [2, 0, 0, 0, 0, 0, 0],
			   [1, 1, 2, 1, 2, 0, 0],
			]

	assert [0, 0, 0, 0, 2, 1] == contenidoColumna(1,tablero)