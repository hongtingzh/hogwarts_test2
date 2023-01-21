import pytest
from python.calc import Calc


class TestCalc:

    def test_add(self):
        calc = Calc()
        result = calc.add(1, 2)
        print(result)
        assert result == 2

    def test_div(self):
        calc = Calc()
        result = calc.div(1, 2)
        print(result)
        assert result == 0.5


if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div'])