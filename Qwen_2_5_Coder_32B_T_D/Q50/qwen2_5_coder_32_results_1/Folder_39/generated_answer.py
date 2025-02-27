from collections import defaultdict

def if_contains_anagrams(strings):
    counts = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            counts[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return anagram_pairs >= 54