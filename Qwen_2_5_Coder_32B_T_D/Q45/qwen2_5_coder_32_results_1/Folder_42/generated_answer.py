from itertools import permutations

def palindromes_between_indices(s):
    letters = [x.lower() for x in s[6:10] if x.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes