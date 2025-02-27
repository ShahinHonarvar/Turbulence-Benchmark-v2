from itertools import permutations

def palindromes_between_indices(s):
    segment = s[:4].lower()
    chars = [char for char in segment if char.isalpha()]
    all_palindromes = set()
    for perm in permutations(chars, len(chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            all_palindromes.add(candidate)
    return all_palindromes