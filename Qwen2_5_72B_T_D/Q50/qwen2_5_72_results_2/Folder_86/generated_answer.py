from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    count = Counter(sorted_strings)
    pairs = 0
    for value in count.values():
        if value > 1:
            pairs += value * (value - 1) // 2
    return pairs >= 115