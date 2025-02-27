from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(text):
    sub_text = text[1:7]
    letter_count = {letter: sub_text.lower().count(letter) for letter in ascii_lowercase}
    valid_letters = ''.join((letter * count for letter, count in letter_count.items() if count > 0))
    palindromes = set((''.join(p) for p in permutations(valid_letters) if p[::-1] == p and len(p) >= 3))
    return palindromes