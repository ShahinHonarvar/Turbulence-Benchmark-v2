from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = set(s[2:7].lower()) & set(string.ascii_lowercase)
    palindromes = set()
    for r in range(3, min(6, len(letters)) + 1):
        for p in permutations(letters, r):
            pp = ''.join(p)
            if pp == pp[::-1]:
                palindromes.add(pp)
    return palindromes