from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:5]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 4):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower():
            palindromes.add(candidate)
    return palindromes