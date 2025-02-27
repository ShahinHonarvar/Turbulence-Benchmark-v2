from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    filtered_chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(filtered_chars, len(filtered_chars)):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 5:
            found_palindromes.add(candidate)
    return found_palindromes