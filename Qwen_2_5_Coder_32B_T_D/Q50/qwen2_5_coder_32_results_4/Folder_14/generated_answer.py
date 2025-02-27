from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_counts[sorted_s] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_of_anagrams >= 22