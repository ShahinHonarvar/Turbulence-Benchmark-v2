from itertools import permutations

def palindromes_between_indices(s):
    letters = [x.lower() for x in s[3:8] if x.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 4:
            palindromes.add(p)
    return palindromes