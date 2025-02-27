from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:8])).lower()
    counter = Counter(letters)
    half = []
    middle = ''
    for char, cnt in counter.items():
        half.extend(char * (cnt // 2))
        if cnt % 2 and (not middle):
            middle = char
    half_perms = set((''.join(p) for p in permutations(half)))
    palindromes = {h + middle + h[::-1] for h in half_perms if len(h) * 2 + len(middle) >= 3}
    return palindromes