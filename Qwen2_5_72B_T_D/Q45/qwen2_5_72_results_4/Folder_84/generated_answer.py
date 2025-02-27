from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[4:10]
    letters = ''.join(filter(str.isalpha, substring.lower()))
    all_perms = {''.join(p) for p in permutations(letters)}
    valid_palindromes = {p for p in all_perms if len(p) >= 3 and is_palindrome(p)}
    return valid_palindromes