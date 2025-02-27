from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_count[s] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pair_count <= 24