from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10].lower()))
    if len(letters) < 7:
        return set()
    count = Counter(letters)
    mid = ''
    half = []
    for letter, freq in count.items():
        half.extend(letter * (freq // 2))
        if freq % 2 and (not mid):
            mid = letter
    if len(half) < (7 - len(mid)) // 2:
        return set()
    half_palindromes = {''.join(p) for p in permutations(half)}
    return {''.join((h, mid, h[::-1])) for h in half_palindromes if len(h) * 2 + len(mid) >= 7}