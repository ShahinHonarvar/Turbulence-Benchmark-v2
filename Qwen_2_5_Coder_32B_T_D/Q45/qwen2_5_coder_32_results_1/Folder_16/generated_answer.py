from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[6:10].lower() if 'a' <= c <= 'z']
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes