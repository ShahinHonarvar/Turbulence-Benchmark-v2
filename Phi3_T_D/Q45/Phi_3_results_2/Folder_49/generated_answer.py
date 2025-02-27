from itertools import permutations
from collections import Counter

def palindromes_between_indices(text):
    substring = text[5:8]
    cnt = Counter(substring.lower())
    palindromes = {''.join(p) for p in permutations(substring.lower()) if not cnt.subtract(p) and (not any((cnt[c] < p.count(c) for c in p)))}
    palindromes = {p for p in palindromes if p == p[::-1] and len(p) >= 3}
    return set(palindromes)