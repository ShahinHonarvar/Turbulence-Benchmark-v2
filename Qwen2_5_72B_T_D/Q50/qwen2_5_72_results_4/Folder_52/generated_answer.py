from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = Counter()
    for s in strings:
        if len(s) >= 3:
            counts[normalize(s)] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in counts.values()))
    return anagram_pairs >= 58