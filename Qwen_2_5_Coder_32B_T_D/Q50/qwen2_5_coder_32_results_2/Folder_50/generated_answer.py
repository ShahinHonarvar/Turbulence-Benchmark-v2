from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            counter[''.join(sorted(s_lower))] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counter.values()))
    return anagram_pairs >= 20