from itertools import permutations

def palindromes_between_indices(s):
    start, end = (8, 9)
    mid = s[start:end + 1]
    length = len(mid)
    palindromes = set()
    if length < 3:
        return palindromes
    mid_lower = mid.lower()
    letters = set(mid_lower)
    for perm in permutations(letters, length):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str.upper())
    return palindromes