from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("El cuadrado de 2 no resultó 4")    # para dar un mensaje más amigable
    
    try:
        assert square(3) == 9
    except AssertionError:
        print("El cuadrado de 3 no resultó 9")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("El cuadrado de -3 no resultó 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("El cuadrado de 0 no resultó 0")


if __name__ == "__main__":
    main()
