from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    sub_s = s[2:6]
    letters = ''.join(filter(str.isalpha, sub_s.lower()))
    if len(letters) < 4:
        return set()
    candidate_palindromes = set((''.join(p) for p in permutations(letters, 4)))
    return set(filter(is_palindrome, candidate_palindromes))