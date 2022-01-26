import unittest
import Calculadora

class PruebasUnitarias(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(Calculadora.Multiplicar(3,4),12)
    def test_dividir(self):
        self.assertEqual(Calculadora.Dividir(12,4),6)

if __name__=='__main__':
    unittest.main()