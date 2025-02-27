import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    charset = set(substring) & set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set((''.join(p) for p in itertools.permutations(charset) if is_palindrome(p)))
    return palindromes