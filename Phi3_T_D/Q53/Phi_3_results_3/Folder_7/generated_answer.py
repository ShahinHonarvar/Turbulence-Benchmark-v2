import re
from itertools import combinations

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    matches = re.findall('(?=([a-z]{122,}))', s.lower())
    palindromes = set(filter(is_palindrome, {''.join(x) for x in combinations(matches, 2)}))
    return palindromes