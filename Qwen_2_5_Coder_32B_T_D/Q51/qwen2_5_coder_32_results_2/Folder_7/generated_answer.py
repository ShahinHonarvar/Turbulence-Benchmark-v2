from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s_cleaned = ''.join(filter(str.isalpha, s.lower()))
        if len(s_cleaned) >= 3:
            sorted_s = ''.join(sorted(s_cleaned))
            anagram_count[sorted_s] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return pair_count <= 445