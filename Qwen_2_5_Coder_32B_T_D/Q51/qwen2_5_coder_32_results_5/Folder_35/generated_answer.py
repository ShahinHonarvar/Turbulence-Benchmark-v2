from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagram_map = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s] += 1
    for value in anagram_map.values():
        count += value * (value - 1) // 2
    return count <= 210