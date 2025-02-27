from itertools import permutations

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def generate_combinations(chars: str) -> set:
    possible_perms = set([''.join(p) for p in permutations(chars)])
    return set(filter(is_palindrome, possible_perms))

def palindromes_between_indices(text: str) -> set:
    substring = text[7:10]
    unique_chars = {char.lower() for char in substring if char.isalpha()}
    if len(unique_chars) < 3:
        return set()
    return generate_combinations(''.join(unique_chars))