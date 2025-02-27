from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_counts[s] += 1
    pairs_of_anagrams = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs_of_anagrams <= 70