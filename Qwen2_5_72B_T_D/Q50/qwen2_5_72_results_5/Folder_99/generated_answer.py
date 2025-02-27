from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = Counter()
    for s in strings:
        if len(s) >= 3:
            counts[normalize(s)] += 1
    pairs = sum((cnt * (cnt - 1) // 2 for cnt in counts.values()))
    return pairs >= 314