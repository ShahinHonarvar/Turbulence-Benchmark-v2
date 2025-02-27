import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:5])).lower()
    palindromes = set()
    for perm in itertools.permutations(s, 4):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes