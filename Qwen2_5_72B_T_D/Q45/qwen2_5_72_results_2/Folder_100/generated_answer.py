from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 6):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes