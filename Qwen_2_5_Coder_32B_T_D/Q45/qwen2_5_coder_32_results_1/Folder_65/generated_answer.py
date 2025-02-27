from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    palindromes = set()
    for perm in permutations(letters, 5):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes