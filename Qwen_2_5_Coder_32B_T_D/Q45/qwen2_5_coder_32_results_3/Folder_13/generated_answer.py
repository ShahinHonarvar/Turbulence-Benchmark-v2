from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    cnt = Counter(letters)
    half = []
    middle = ''
    for l in cnt:
        if cnt[l] // 2 > 0:
            half += [l] * (cnt[l] // 2)
        if cnt[l] % 2 == 1 and (not middle):
            middle = l
    palindromes = set()
    for p in itertools.permutations(half):
        palindromes.add(''.join(p) + middle + ''.join(reversed(p)))
    return {p for p in palindromes if len(p) >= 5}