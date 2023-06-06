from calculator import square

def main():
    # test_square()
    test_square_negatives()
    test_square_positives()
    test_square_zero()


"""
Podemos hacer todas las aserciones en una sola función teniendo un sólo test.
"""
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-3) == 9
#     assert square(0) == 0


"""
O tener las aserciones segmentadas para validar diferentes tests.
"""
def test_square_positives():
    assert square(2) == 4
    assert square(3) == 9

def test_square_negatives():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0

if __name__ == "__main__":
    main()
