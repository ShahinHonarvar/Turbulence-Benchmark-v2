from itertools import combinations
    from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_chars(s)
            anagram_count[key] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values() if v >= 2))
    return pair_count >= 68