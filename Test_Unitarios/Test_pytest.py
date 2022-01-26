import pytest
import Calculadora

# Comprobación valida
def test_sumar():
    x =3
    y =5
    resultado = 8
    assert resultado == Calculadora.Sumar(x,y)

# Comprobación Invalida
def test_restar():
    x =8
    y =2
    resultado = 1
    assert resultado == Calculadora.Restar(x,y)