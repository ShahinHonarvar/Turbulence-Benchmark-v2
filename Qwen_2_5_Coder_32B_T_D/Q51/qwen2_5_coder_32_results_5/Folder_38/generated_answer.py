from collections import Counter

def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    anagram_counts = Counter(lst)
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values() if v > 1))
    return anagram_pairs <= 416