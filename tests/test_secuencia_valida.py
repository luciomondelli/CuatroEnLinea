from src.CuatroEnLinea import columnaValida

def test_columna_Valida():
	secuencia = [1, 2, 6, 2, 5, 4, 2]

	assert columnaValida(secuencia) == True