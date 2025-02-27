from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    sorted_strings = [''.join(sorted(s)) for s in strings if len(s) >= 3]
    counts = Counter(sorted_strings)
    pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return pairs >= 78