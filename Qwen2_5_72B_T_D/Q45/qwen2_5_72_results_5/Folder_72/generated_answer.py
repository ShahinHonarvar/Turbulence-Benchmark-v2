from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    chars = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(chars, 6):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes