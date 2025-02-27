from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[4:10]
    substring_perms = set((''.join(p) for p in permutations(substring.lower()) if ''.join(p).isalpha()))
    palindromes = {word for word in substring_perms if len(word) >= 3 and is_palindrome(word)}
    return palindromes