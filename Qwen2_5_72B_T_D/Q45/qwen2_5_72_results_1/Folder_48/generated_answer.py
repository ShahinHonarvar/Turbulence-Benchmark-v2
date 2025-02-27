from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9]
    unique_chars = set(substring.lower())
    possible_palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        candidate = ''.join(perm) * 2
        if candidate == candidate[::-1]:
            possible_palindromes.add(candidate)
    return possible_palindromes