from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    unique_chars = {c.lower() for c in s[3:10]}
    char_permutations = set((''.join(p) for l in range(7, 10) for p in permutations(sorted(unique_chars), l)))
    palindromes = {p for p in char_permutations if is_palindrome(p)}
    return palindromes