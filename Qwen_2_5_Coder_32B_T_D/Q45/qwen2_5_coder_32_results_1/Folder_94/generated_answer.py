from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:5].lower()))
    c = Counter(letters)
    if len(letters) < 2 or len(c) < 2:
        return set()
    half = []
    middle = []
    for k, v in c.items():
        half += [k] * (v // 2)
        if v % 2:
            middle.append(k)
    palindromes = set()
    for h in set(permutations(half)):
        for m in middle:
            palindromes.add(''.join(h) + m + ''.join(reversed(h)))
    if not middle:
        for h in set(permutations(half)):
            palindromes.add(''.join(h) + ''.join(reversed(h)))
    return {p for p in palindromes if len(p) >= 3}