# Viene con Python
import unittest


# Todas mis pruebas o subconjuntos de pruebas los voy a tener en una clase.
class OtrasPruebas(unittest.TestCase):

    def test_suma_ex(self):
        a = 2 + 4
        b = 3 + 3
        self.assertEqual(a, b)

    def test_otra_suma_ex(self):
        a = 5 + 2
        b = 7
        self.assertNotEqual(5+1, 8)

    def test_algo_es_verdadero_ex(self):
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a == b, "a y b deberían ser iguales")