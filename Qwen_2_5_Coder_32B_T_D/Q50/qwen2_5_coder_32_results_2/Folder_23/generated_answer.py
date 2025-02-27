import collections

def if_contains_anagrams(strings):
    count_map = collections.defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            count_map[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count_map.values() if v > 1))
    return anagram_pairs >= 67