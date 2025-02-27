from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [c for c in s if c.isalpha()]
    counter = Counter(letters)
    mid = ''
    sides = []
    for char, count in counter.items():
        if count % 2 == 1:
            if mid:
                return set()
            mid = char
        sides.extend(char * (count // 2))
    side_perms = set([''.join(p) for p in permutations(sides)])
    palindromes = set([side + mid + side[::-1] for side in side_perms if len(side) * 2 + len(mid) >= 3])
    return palindromes