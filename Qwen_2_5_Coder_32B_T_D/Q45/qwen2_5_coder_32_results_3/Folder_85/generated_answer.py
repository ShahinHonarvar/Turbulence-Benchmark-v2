from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:9])).lower()
    c = Counter(letters)
    if len(letters) < 7:
        return set()
    mid = ''
    sides = []
    for k, v in c.items():
        mid += k * (v % 2)
        sides += k * (v // 2)
    if len(mid) > 1:
        return set()
    palindromes = set()
    for side in set(permutations(sides, len(sides))):
        palindromes.add(''.join(side) + mid + ''.join(reversed(side)))
    return {p for p in palindromes if len(p) >= 7}