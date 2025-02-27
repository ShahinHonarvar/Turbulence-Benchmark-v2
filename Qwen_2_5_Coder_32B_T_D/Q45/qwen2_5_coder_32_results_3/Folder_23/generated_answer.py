import itertools
    import string

def palindromes_between_indices(s):
    letters = set(s[:7].lower()) & set(string.ascii_lowercase)
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for comb in itertools.permutations(letters, r):
            candidate = ''.join(comb)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes