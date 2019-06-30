# /usr/bin/env python3

import tiles

# return a python list of the full scrabble wordlist
def load_wordlist(path="wordlist.txt"):
    with open(path) as opened_file:
        words = opened_file.read().splitlines()

    return words


def score_word(word):
    return sum([tiles.Tile(i) for i in word])


# only run this bit if it's called as
# `python utils.py` but NOT if it's imported as
# `import utils` from another py file
if __name__ == "__main__":
    pass
