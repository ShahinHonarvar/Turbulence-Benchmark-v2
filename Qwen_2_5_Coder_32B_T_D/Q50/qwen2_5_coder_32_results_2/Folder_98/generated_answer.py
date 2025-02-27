from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            anagram_counts[''.join(sorted(s))] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pair_count >= 7