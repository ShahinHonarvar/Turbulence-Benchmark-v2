from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:10])).lower()
    counts = Counter(letters)
    mid = ''
    sides = []
    for char, count in counts.items():
        if count % 2:
            mid = char
            count -= 1
        sides.extend(char * (count // 2))
    if len(sides) < 3:
        return set()
    side_perms = set((''.join(p) for p in permutations(sides, 3)))
    return {sp + mid + sp[::-1] for sp in side_perms}