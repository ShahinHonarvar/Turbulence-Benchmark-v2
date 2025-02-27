from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_count[s] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs <= 73