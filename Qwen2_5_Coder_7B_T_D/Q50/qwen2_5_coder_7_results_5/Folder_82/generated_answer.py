from collections import Counter

def if_contains_anagrams(lst):
    counts = Counter()
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            counts[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counts.values() if v > 1))
    return anagram_pairs >= 276