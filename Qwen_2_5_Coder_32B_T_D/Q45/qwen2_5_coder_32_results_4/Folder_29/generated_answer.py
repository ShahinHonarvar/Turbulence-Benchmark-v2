from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    seen = set()
    pali_set = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if perm_str not in seen:
            seen.add(perm_str)
            rev = perm_str[::-1]
            if perm_str == rev and len(perm_str) >= 6:
                pali_set.add(perm_str)
    return pali_set