from itertools import permutations

def palindromes_between_indices(s):
    start, end = (2, 3)
    chars = [c.lower() for c in s[start:end + 1] if c.isalpha()]
    if len(chars) < 3:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    all_perms = {''.join(p) for p in permutations(chars)}
    palindromes = {p for p in all_perms if is_palindrome(p)}
    return palindromes