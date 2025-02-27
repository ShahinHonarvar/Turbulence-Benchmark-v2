import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    perms = set(itertools.permutations(letters))
    palindromes = set()
    for p in perms:
        candidate = ''.join(p)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes