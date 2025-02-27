from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[1:6]
    perms = {''.join(p) for p in set(permutations(substring.lower()))}
    palindromes = {p for p in perms if len(p) >= 4 and is_palindrome(p)}
    return palindromes