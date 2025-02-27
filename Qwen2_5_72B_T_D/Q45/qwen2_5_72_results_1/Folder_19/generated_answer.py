from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 7:
            palindromes.add(candidate)
    return palindromes