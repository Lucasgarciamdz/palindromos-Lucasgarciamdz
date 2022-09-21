import unittest
from palindromos import capicua


class TestCapicua(unittest.TestCase):

    def test_capicua(self):
        self.assertTrue(capicua("ana"))
        self.assertTrue(capicua("reconocer"))
        self.assertFalse(capicua("hola"))
        self.assertFalse(capicua("palabra"))

    def test_not_capicua(self):
        self.assertFalse(capicua("hola"))
        self.assertFalse(capicua("palabra"))

    def test_sentence(self):
        self.assertTrue(capicua("anita lava la tina"))

    def test_capital_letters(self):
        self.assertTrue(capicua("Ana"))
        self.assertTrue(capicua("Reconocer"))
        self.assertFalse(capicua("Hola"))
    
    def test_not_capicua_sentence(self):
        self.assertFalse(capicua("Hola mundo"))
        self.assertFalse(capicua("Palabra larga"))
        
if __name__ == "__main__":
    unittest.main()