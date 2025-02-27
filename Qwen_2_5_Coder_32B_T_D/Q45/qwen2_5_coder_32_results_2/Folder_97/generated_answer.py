from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:5])).lower()
    cnt = Counter(letters)
    mid, sides = ('', [])
    for char, freq in cnt.items():
        if freq % 2:
            mid = char
        sides.extend(char * (freq // 2))
    palindromes = set()
    for side in set((''.join(p) for p in permutations(sides))):
        palindromes.add(side + mid + side[::-1])
    return {p for p in palindromes if len(p) >= 3}