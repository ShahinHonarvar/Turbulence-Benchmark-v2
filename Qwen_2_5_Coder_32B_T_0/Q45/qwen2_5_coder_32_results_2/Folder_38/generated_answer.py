from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes