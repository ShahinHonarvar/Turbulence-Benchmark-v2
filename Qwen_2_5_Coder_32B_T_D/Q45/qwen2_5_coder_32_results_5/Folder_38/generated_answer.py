from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes