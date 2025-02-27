from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    substring = text[3:8].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes