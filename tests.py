import unittest

import utils
import tiles

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.wordlist = utils.load_wordlist()

    def test_load_wordlist(self):
        self.assertEqual(self.wordlist[0], 'aa')
        self.assertEqual(self.wordlist[-1], 'zyzzyvas')
        self.assertEqual(len(self.wordlist), 172820)

    # no explicit assertion.
    # This test fails if the addition inside raises an exception
    def test_add_letters(self):
        tiles.letters['a'] + tiles.letters['b']

    def test_score_word(self):
        test_words = [('farts', 8), ('quixotic', 26), ('chutzpah', 27), ('adamginsberg', 19)]

        for test_word, expected_score in test_words:
            calculated_score = utils.score_word(test_word)
            self.assertEqual(calculated_score, expected_score)


if __name__ == '__main__':
    unittest.main()
