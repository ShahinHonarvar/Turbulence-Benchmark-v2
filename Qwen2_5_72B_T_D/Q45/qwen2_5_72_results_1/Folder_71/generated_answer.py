from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:4]
    chars = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(chars, len(chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes