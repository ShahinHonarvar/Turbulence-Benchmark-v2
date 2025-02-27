from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8]
    letters = ''.join(filter(str.isalpha, s)).lower()
    count = Counter(letters)
    mid = ''
    sides = []
    for letter, cnt in count.items():
        mid += letter * (cnt % 2)
        sides.append(letter * (cnt // 2))
    if len(mid) > 1:
        return set()
    mid = mid[0] if mid else ''
    palindromes = set()
    for side in set(permutations(''.join(sides))):
        palindromes.add(''.join(side) + mid + ''.join(reversed(side)))
    return {p for p in palindromes if len(p) >= 4}