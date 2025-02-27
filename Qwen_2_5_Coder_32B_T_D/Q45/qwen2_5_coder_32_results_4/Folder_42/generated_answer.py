from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes