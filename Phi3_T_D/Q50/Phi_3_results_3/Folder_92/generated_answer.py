from collections import Counter

def if_contains_anagrams(strings):
    count = Counter((''.join(sorted(s.lower())) for s in strings if len(s) >= 3))
    return any((v >= 2 for v in count.values()))