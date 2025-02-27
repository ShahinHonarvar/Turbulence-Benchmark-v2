from itertools import permutations

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(s: str) -> set:
    sub = s[2:4]
    unique_chars = set(sub.lower())
    palindromes = set()
    for n in range(3, len(unique_chars) + 1):
        for p in permutations(unique_chars, n):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes