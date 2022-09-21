import unittest




def capicua(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


if __name__ == "__main__":
    unittest.main()
