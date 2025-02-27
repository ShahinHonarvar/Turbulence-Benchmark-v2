from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()
    c = Counter(letters)
    if len(letters) < 3:
        return set()
    mid = ''
    half = []
    for k, v in c.items():
        if v % 2:
            if mid:
                return set()
            mid = k
        half.extend(k * (v // 2))
    palindromes = set()
    for p in set(permutations(half)):
        palindromes.add(''.join(p) + mid + ''.join(p[::-1]))
    return palindromes