"""Peer Review Assignment - Developers"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglish2French(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('I love you'), 'Je t\'aime')
        self.assertNotEqual(english_to_french('Good night'), 'Au revoir')


class TestFrench2English(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(' '), ' ')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Je t\'aime'), 'I love you')
        self.assertNotEqual(french_to_english('Au revoir'), 'Good night')

unittest.main()
