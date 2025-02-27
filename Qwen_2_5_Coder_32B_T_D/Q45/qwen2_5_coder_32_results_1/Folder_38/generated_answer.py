from itertools import permutations

def palindromes_between_indices(s):
    chars = ''.join(filter(str.isalpha, s[3:9])).lower()
    palindromes = set()
    for perm in permutations(chars):
        p = ''.join(perm)
        if len(p) >= 5 and p == p[::-1]:
            palindromes.add(p)
    return palindromes