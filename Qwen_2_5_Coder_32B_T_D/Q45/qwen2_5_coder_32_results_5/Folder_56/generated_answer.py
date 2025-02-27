from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:10])).lower()
    ctr = Counter(letters)
    mid, sides = ('', [])
    for letter, count in ctr.items():
        mid += letter * (count % 2)
        sides.extend(letter * (count // 2))
    if len(mid) > 1:
        return set()
    palindromes = set()
    for side in set(permutations(sides)):
        palindromes.add(''.join(side) + mid + ''.join(reversed(side)))
    return {p for p in palindromes if len(p) >= 5}