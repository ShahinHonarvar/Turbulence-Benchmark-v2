from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:4]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes