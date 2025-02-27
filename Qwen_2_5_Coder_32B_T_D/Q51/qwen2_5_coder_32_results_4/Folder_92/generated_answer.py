from collections import defaultdict

def if_contains_anagrams(lst):
    counts = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        counts[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return anagram_pairs <= 34