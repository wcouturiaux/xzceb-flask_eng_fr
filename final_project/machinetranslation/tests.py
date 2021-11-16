from translator import *
import unittest

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual("Hello","Bonjour")
        self.assertEqual("","")

    def test_frenchToEnglish(self):
        self.assertEqual("Bonjour","Hello")
        self.assertEqual("","")