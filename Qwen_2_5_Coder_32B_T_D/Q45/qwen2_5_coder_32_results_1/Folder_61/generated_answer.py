from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[:8] if c.isalpha()])
    count = Counter(letters)
    mid, half = ('', [])
    for c in count:
        if count[c] % 2:
            mid = c
            half.append(c * (count[c] // 2))
        else:
            half.append(c * (count[c] // 2))
    half = ''.join(half)
    palindromes = set()
    for p in itertools.permutations(half):
        p = ''.join(p)
        palindromes.add(p + mid + p[::-1])
    return {p for p in palindromes if len(p) >= 7}