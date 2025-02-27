from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    sorted_strings = [''.join(sorted(s)) for s in strings if len(s) >= 3]
    count = Counter(sorted_strings)
    pairs = 0
    for c in count.values():
        if c > 1:
            pairs += c * (c - 1) // 2
    return pairs >= 67