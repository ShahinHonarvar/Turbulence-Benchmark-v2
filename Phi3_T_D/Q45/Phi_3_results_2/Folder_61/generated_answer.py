from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[:8].lower()
    letters = ''.join(set(substring))
    palindromes = set()
    if len(letters) < 7:
        return palindromes
    for p in permutations(letters, 7):
        candidate = ''.join(p)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes