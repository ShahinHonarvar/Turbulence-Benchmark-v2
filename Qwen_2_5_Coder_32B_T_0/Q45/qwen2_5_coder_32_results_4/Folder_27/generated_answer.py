from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:9])).lower()
    palindromes = set()
    for perm in permutations(letters, 6):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes