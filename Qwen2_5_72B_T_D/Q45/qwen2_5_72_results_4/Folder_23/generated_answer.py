from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7].lower()
    all_chars = ''.join([c for c in substring if c.isalpha()])
    found_palindromes = set()
    for p in permutations(all_chars, 4):
        candidate = ''.join(p)
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes