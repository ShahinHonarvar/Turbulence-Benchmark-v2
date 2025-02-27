from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    counts = Counter(sorted_strings)
    pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return pairs >= 70