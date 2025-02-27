from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    palindromes = set()
    for perm in permutations(letters, 5):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes