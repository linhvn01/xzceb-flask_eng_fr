import unittest
from translator import french_to_english
from translator import english_to_french

class Translator(unittest.TestCase):


    def test_french_to_english(self):
            self.assertTrue("".__eq__(french_to_english("")))
            self.assertEqual(french_to_english("Bonjour"),"Hello")

    def test_english_to_french(self):
            self.assertTrue("".__eq__(english_to_french("")))
            self.assertEqual(english_to_french("Hello"),"Bonjour")

if __name__ == '__main__':
    unittest.main()