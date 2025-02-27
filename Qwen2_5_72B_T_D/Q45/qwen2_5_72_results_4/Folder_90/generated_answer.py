from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes