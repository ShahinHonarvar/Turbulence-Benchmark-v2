import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[:8] if c.isalpha()])
    letter_counts = Counter(letters)
    mid = []
    half = []
    for letter, count in letter_counts.items():
        mid += [letter] * (count % 2)
        half += [letter] * (count // 2)
    palindromes = set()
    if len(mid) < 2:
        for perm in itertools.permutations(half):
            p = ''.join(perm) + (mid[0] if mid else '') + ''.join(reversed(perm))
            palindromes.add(p)
    return {p for p in palindromes if len(p) >= 6}