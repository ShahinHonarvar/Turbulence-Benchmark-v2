from itertools import permutations
from collections import Counter

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(s: str) -> set:
    counter = Counter(s.lower()[:8])
    chars = ''.join([k * v for k, v in counter.items() if k.isalpha()])
    palindromes = {''.join(p) for p in permutations(chars, len(chars)) if is_palindrome(p[0] + p[-1])}
    return {p for p in palindromes if len(p) >= 7}