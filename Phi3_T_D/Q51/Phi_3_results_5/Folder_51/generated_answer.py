from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    anagram_pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_map[sorted_s].append(s)
    for _, v in anagram_map.items():
        if len(v) > 1:
            anagram_pairs += len(v) * (len(v) - 1) // 2
    return anagram_pairs <= 116