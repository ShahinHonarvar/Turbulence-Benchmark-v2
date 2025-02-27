from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(str.isalpha, s[4:6].lower())))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes