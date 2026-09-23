import pytest
from src.ejercicios import fizzbuzz, expand, list2num

class TestFizzBuzz:
    def test_fizzbuzz_longitud(self):
        resultado = fizzbuzz()
        assert len(resultado) == 100

    def test_fizzbuzz_casos_clave(self):
        res = fizzbuzz()
        assert res[0] == "1"            # Posición 1
        assert res[2] == "Fizz"         # Posición 3 (divisible por 3)
        assert res[4] == "Buzz"         # Posición 5 (divisible por 5)
        assert res[14] == "FizzBuzz"    # Posición 15 (divisible por 3 y 5)


class TestExpansivos:
    @pytest.mark.parametrize("entrada,esperado", [
        ([1], [1, 1]),               # 1 -> "11"
        ([1, 1], [2, 1]),            # 11 -> "21"
        ([2, 1], [1, 2, 1, 1]),      # 21 -> "1211"
        ([1, 2, 1, 1], [1, 1, 1, 2, 2, 1]), # 1211 -> "111221"
        ([3, 3, 3, 3], [4, 3])       # Ejemplo de la consigna
    ])
    def test_expand(self, entrada, esperado):
        assert expand(entrada) == esperado

    def test_expand_vacio(self):
        assert expand([]) == []

    @pytest.mark.parametrize("entrada,esperado", [
        ([1], 1),
        ([1, 1], 11),
        ([2, 1], 21),
        ([1, 2, 1, 1], 1211),
        ([1, 1, 1, 2, 2, 1], 111221)
    ])
    def test_list2num(self, entrada, esperado):
        assert list2num(entrada) == esperado

    def test_list2num_vacio(self):
        assert list2num([]) == 0