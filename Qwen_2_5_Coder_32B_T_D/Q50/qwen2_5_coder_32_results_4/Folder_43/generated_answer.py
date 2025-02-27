from collections import Counter

def if_contains_anagrams(lst):
    anagram_counts = Counter((''.join(sorted(s.lower())) for s in lst if len(s) >= 3))
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 61