import itertools

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(s: str) -> set:
    substring = s[0:8].lower()
    letters = ''.join(sorted(set(substring), key=substring.index))
    palindromes = {''.join(p) for p in itertools.permutations(letters, 6) if is_palindrome(''.join(p))}
    return palindromes