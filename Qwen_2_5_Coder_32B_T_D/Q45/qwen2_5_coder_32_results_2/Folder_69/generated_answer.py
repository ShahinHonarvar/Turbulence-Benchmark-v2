from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    counter = Counter(letters)
    mid, sides = ('', '')
    for l, cnt in counter.items():
        if cnt % 2:
            if mid:
                break
            mid = l
        sides += l * (cnt // 2)
    else:
        palindromes = set()
        for perm in set(itertools.permutations(sides)):
            palindromes.add(''.join(perm) + mid + ''.join(reversed(perm)))
        return palindromes
    return set()