from itertools import permutations

def palindromes_between_indices(s):
    letters = []
    for i in range(1, 7):
        if ord('a') <= ord(s[i].lower()) <= ord('z'):
            letters.append(s[i].lower())
    unique_perms = set((''.join(p) for i in range(7, len(letters) + 1) for p in permutations(letters, i)))
    palindromes = {p for p in unique_perms if p == p[::-1]}
    return palindromes