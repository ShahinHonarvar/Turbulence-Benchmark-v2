from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:8])).lower()
    count = Counter(letters)
    mid, sides = ('', '')
    for char, freq in count.items():
        sides += char * (freq // 2)
        if freq % 2 and (not mid):
            mid = char
    perms = set([''.join(p) for p in permutations(sides)])
    return {p + mid + p[::-1] for p in perms if len(p) * 2 + len(mid) >= 6}