from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes