import math
import pytest
from fin_utils import (
    interes_simple, tasa_diaria,
    interes_compuesto_diario, comparar_lineal_vs_compuesto
)

def test_interes_simple_basico():
    assert math.isclose(interes_simple(10000, 12.5, 30), 102.739726, rel_tol=1e-9)

@pytest.mark.parametrize("tasa", [0, 8, 50])
def test_tasa_diaria_no_negativa(tasa):
    td = tasa_diaria(tasa)
    assert td >= 0

def test_tasa_diaria_negativa():
    with pytest.raises(ValueError):
        tasa_diaria(-1)

def test_compuesto_vs_lineal():
    lin, comp, diff = comparar_lineal_vs_compuesto(10000, 8, 20)
    assert comp < lin and diff > 0

def test_entradas_invalidas():
    with pytest.raises(ValueError):
        interes_simple(0, 10, 10)
    with pytest.raises(ValueError):
        interes_compuesto_diario(100, 10, 0)