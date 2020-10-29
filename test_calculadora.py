from unittest import TestCase
from calculadora import calculadora_simples

class TestCalculadora(TestCase):
    # Soma
    def test_soma_true(self):
        resultado = calculadora_simples(2, 2, '+')
        self.assertEqual(resultado, 4)

    def test_soma_false(self):
        resultado = calculadora_simples(2, 3, '+')
        self.assertNotEqual(resultado, 4)

    def test_soma_type_float(self):
        resultado = calculadora_simples(2, 3.4, '+')
        self.assertEqual(type(resultado), float)

    def test_soma_type_int(self):
        resultado = calculadora_simples(2, 3, '+')
        self.assertEqual(type(resultado), int)

    # Subtração
    def test_subtracao_true(self):
        resultado = calculadora_simples(4, 2, '-')
        self.assertEqual(resultado, 2)

    def test_subtracao_false(self):
        resultado = calculadora_simples(2, 3, '-')
        self.assertNotEqual(resultado, 4)

    def test_subtracao_type_float(self):
        resultado = calculadora_simples(6, 3.4, '-')
        self.assertEqual(type(resultado), float)

    def test_subtracao_type_int(self):
        resultado = calculadora_simples(2, 3, '-')
        self.assertEqual(type(resultado), int)

    # Multiplicação
    def test_multiplicacao_true(self):
        resultado = calculadora_simples(4, 2, '*')
        self.assertEqual(resultado, 8)

    def test_multiplicacao_false(self):
        resultado = calculadora_simples(2, 3, '*')
        self.assertNotEqual(resultado, 5)

    def test_multiplicacao_type_float(self):
        resultado = calculadora_simples(6, 3.4, '*')
        self.assertEqual(type(resultado), float)

    def test_multiplicacao_type_int(self):
        resultado = calculadora_simples(2, 3, '*')
        self.assertEqual(type(resultado), int)

    # Divisão
    def test_divisao_true(self):
        resultado = calculadora_simples(4, 2, '/')
        self.assertEqual(resultado, 2)

    def test_divisao_false(self):
        resultado = calculadora_simples(6, 3, '/')
        self.assertNotEqual(resultado, 5)

    def test_divisao_type_float(self):
        resultado = calculadora_simples(6, 3.4, '/')
        self.assertEqual(type(resultado), float)

    # Exponenciação
    def test_exponenciacao_true(self):
        resultado = calculadora_simples(4, 2, '**')
        self.assertEqual(resultado, 16)

    def test_exponenciacao_false(self):
        resultado = calculadora_simples(6, 3, '**')
        self.assertNotEqual(resultado, 5)

    def test_exponenciacao_type_float(self):
        resultado = calculadora_simples(6, 3.4, '**')
        self.assertEqual(type(resultado), float)

    def test_exponenciacao_type_int(self):
        resultado = calculadora_simples(8, 4, '**')
        self.assertEqual(type(resultado), int)

    # Módulo
    def test_modulo_true(self):
        resultado = calculadora_simples(4, 2, '%')
        self.assertEqual(resultado, 0)

    def test_modulo_false(self):
        resultado = calculadora_simples(6, 5, '%')
        self.assertNotEqual(resultado, 0)

    def test_modulo_type_float(self):
        resultado = calculadora_simples(6, 3.4, '%')
        self.assertEqual(type(resultado), float)

    def test_modulo_type_int(self):
        resultado = calculadora_simples(8, 4, '%')
        self.assertEqual(type(resultado), int)