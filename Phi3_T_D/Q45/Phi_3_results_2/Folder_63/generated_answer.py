from itertools import permutations

def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s: str) -> set:
    sub_str = s[:4].lower()
    palindromes = set()
    if len(sub_str) < 3:
        return palindromes
    for perm in permutations(sub_str):
        if is_palindrome(''.join(perm)):
            palindromes.add(''.join(perm))
    return palindromes