from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            anagram_count[s_sorted] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pair_count >= 65