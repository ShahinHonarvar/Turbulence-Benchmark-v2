from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[5:10] if c.isalpha()]))
    counts = Counter(letters)
    mid = ''.join([char for char, count in counts.items() if count % 2 == 1])
    sides = ''.join([char * (count // 2) for char, count in counts.items()])
    palindromes = set()
    if len(mid) <= 1:
        for side in set([''.join(p) for p in permutations(sides)]):
            if len(letters) % 2 == 0:
                palindromes.add(side + side[::-1])
            else:
                palindromes.add(side + mid + side[::-1])
    return {p for p in palindromes if len(p) >= 6}