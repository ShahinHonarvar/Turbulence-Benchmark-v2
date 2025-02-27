from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_count[sorted_s] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in anagram_count.values() if c >= 2))
    return anagram_pairs >= 3