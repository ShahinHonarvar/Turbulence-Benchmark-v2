from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    unique_chars = set(substring)
    found_palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            found_palindromes.add(candidate)
    return found_palindromes