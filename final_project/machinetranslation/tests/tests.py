import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    '''
    Test English to French translation
    '''
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')

    def test2(self):
        self.assertNotEqual(english_to_french('hello'), 'hello')


class TestFrenchToEnglish(unittest.TestCase):
    '''
    Test French to English translation
    '''
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')

    def test2(self):
        self.assertNotEqual(english_to_french('bonjour'), 'bonjour')


unittest.main()
