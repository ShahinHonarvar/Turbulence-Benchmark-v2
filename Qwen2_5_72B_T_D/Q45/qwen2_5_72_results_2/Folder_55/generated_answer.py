from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:3].lower()
    unique_chars = set(substring)
    all_palindromes = set()
    for r in range(3, len(substring) + 1):
        for perm in permutations(unique_chars, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                all_palindromes.add(candidate)
    return all_palindromes