from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:8]]
    perms = set(permutations(letters))
    palindromes = set()
    for perm in perms:
        candidate = ''.join(perm).capitalize()
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes