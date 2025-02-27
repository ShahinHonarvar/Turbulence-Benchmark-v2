import itertools

def palindromes_between_indices(s):
    sliced = s[6:10]
    letters = set(sliced.lower())
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for length in range(3, len(sliced) + 1):
        perms = itertools.permutations(letters, length)
        for perm in perms:
            str_perm = ''.join(perm)
            if str_perm == str_perm[::-1]:
                palindromes.add(str_perm)
    return palindromes