from translator import *
import unittest

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual("","")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual("","")

if __name__ == '__main__':
    unittest.main()
    