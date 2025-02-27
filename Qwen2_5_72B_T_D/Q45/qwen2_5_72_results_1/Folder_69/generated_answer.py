from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:4].lower()
    chars = [char for char in substring if char.isalpha()]
    all_palindromes = set()
    for combo in permutations(chars, len(chars)):
        candidate = ''.join(combo)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            all_palindromes.add(candidate)
    return all_palindromes