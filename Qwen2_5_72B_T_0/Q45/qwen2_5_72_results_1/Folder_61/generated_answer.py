from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 7):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes