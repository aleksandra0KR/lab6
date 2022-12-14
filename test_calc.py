import calc


def test_plus1():
    output = calc.calc("3 + 4")
    assert output == 7


def test_plus2():
    output = calc.calc("3 - 4")
    assert output == -1


def test_plus3():
    output = calc.calc("3 * 4")
    assert output == 12
    
test_plus1()
test_plus2()
test_plus3()
