from src.CuatroEnLinea import Filas

def test_Filas():

	tablero = [[0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0],
			   [1, 0, 0, 0, 0, 0, 1],
			  ]

	assert Filas(tablero) == [[1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],]