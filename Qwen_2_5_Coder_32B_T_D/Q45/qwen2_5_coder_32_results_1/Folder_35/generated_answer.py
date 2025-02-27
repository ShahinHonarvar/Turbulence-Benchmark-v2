import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:5])).lower()
    if len(letters) < 4:
        return set()
    letter_counts = Counter(letters)
    mid = ''
    sides = []
    for letter, count in letter_counts.items():
        mid += letter * (count % 2)
        sides.append(letter * (count // 2))
    if len(mid) > 1:
        return set()
    mid = mid[0] if mid else ''
    sides = ''.join(sides)
    palindromes = set()
    for p in set(itertools.permutations(sides)):
        p = ''.join(p)
        palindromes.add(p + mid + p[::-1])
    return palindromes