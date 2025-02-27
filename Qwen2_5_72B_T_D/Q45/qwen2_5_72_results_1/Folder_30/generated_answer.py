from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:5]
    chars = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(chars, 4):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes