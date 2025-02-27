from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    count = Counter(letters)
    mid, sides = ('', '')
    for char, cnt in count.items():
        mid += char * (cnt % 2)
        sides += char * (cnt // 2)
    if len(mid) > 1:
        return set()
    palindromes = set()
    for side in set((''.join(p) for p in permutations(sides))):
        palindromes.add(side + mid + side[::-1])
    return palindromes