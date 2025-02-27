from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_groups = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_groups[sorted_s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_groups.values() if len(v) > 1))
    return anagram_pairs <= 40