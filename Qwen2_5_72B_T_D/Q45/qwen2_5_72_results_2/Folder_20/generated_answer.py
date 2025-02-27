from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9]
    chars = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(4, len(chars) + 1):
        for perm in permutations(chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes