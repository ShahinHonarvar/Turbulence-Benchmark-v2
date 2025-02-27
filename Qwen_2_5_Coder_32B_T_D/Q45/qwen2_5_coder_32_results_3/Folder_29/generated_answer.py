from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 6:
        return set()
    c = Counter(s)
    mid = ''
    sides = []
    for char, count in c.items():
        if count % 2 == 1 and mid == '':
            mid = char
            count -= 1
        sides.extend(char * (count // 2))
    if len(sides) < 3:
        return set()
    palindromes = set()
    for p in set(permutations(sides, len(sides))):
        palindromes.add(''.join(p) + mid + ''.join(reversed(p)))
    return palindromes