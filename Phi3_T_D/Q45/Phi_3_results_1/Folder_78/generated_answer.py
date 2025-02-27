from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower() and len(word) >= 3
    letters = s[6:9]
    all_perms = set((''.join(p) for p in permutations(letters)))
    return set(filter(is_palindrome, all_perms))