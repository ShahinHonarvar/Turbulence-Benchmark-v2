from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:9])).lower()
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 3 and p == p[::-1]:
            palindromes.add(p)
    return palindromes