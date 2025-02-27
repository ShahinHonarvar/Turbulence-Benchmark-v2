from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [c for c in s if 'a' <= c <= 'z']
    pali_set = set()
    for perm in permutations(letters, min(5, len(letters))):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            pali_set.add(p)
    return pali_set