from src.CuatroEnLinea import tableroVacio
def test_tablero_vacio_tiene_6_filas_y_7_columnas():
	tablero = tableroVacio()

	assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
	tablero = tableroVacio()

	assert len(tablero[0]) == 7