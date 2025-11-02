from src.propinas import calcular_propina


def test_calcular_propina_basica():
    assert calcular_propina(100, 10) == 10.0


def test_calcular_propina_decimales():
    assert calcular_propina(123.45, 15) == round(123.45 * 0.15, 2)
