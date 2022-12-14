import calc
class Tests:

    def test_plus(self):
        output = calc.calc("3 + 4")
        assert output == 12
        
    def test_plus(self):
        output = calc.calc("3 - 4")
        assert output == -1
        
    def test_plus(self):
        output = calc.calc("3 * 4")
        assert output == 16

