from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    start, end = (3, 9)
    substring = (s[i] for i in range(start, end + 1))
    sub_string = ''.join(sorted((char.upper() for char in substring if char.isalpha())))
    if len(sub_string) < 2:
        return set()
    return set((p for p in permutations(sub_string) if is_palindrome(p) and len(p) >= 3))