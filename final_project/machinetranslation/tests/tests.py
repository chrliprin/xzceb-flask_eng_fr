import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('good bye'), 'Au revoir')
        self.assertNotEqual(english_to_french('How are you?'), 'Come stai?')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertNotEqual(french_to_english('Au revoir'), 'Come stai?')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
unittest.main()