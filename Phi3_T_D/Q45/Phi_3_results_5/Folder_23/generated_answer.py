from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1] and len(word) > 3
    substring = s[0:7].lower()
    letters = set(substring)
    possible_palindromes = set((''.join(p) for p in permutations(letters) if len(p) >= 4 and is_palindrome(''.join(p))))
    return possible_palindromes