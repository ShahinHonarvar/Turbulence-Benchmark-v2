from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    all_chars = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(7, len(all_chars) + 1):
        for perm in permutations(all_chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes