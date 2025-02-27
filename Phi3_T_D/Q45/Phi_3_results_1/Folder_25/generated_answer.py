from itertools import permutations

def palindromes_between_indices(s):
    window = s[1:5]
    window = ''.join([c.lower() for c in window if c.isalpha()])
    palindromes = set()
    for perm_len in range(3, len(window) + 1):
        for perm in permutations(window, perm_len):
            cand = ''.join(perm)
            if cand == cand[::-1]:
                palindromes.add(cand)
    return palindromes