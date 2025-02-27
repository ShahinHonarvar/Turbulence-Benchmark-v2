from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5]
    chars = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in set(permutations(chars)):
        candidate = ''.join(perm)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes