import unittest
from main import make_upper_case

class TestStringMethods(unittest.TestCase):
    def test_upper_case(self):
        test_words = {
            "word": "WORD",
            "hola": "HOLA",
            "HELLO": "HELLO",
            "": ""
        }

        for input_, output_ in test_words.items():
            self.assertEqual(make_upper_case(input_), output_)

